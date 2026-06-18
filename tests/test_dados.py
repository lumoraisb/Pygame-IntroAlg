import os
import tempfile
import pytest

from src.dados import salvar_partida, carregar_historico, RANKING_PATH


@pytest.fixture
def arquivo_temporario(monkeypatch, tmp_path):
    #redireciona o caminho do ranking para um arquivo temporário durante os testes
    caminho = tmp_path / "ranking.txt"
    monkeypatch.setattr("src.dados.RANKING_PATH", str(caminho))
    return caminho


def test_salvar_partida(arquivo_temporario):
    salvar_partida(1, 2, 0, 3)
    conteudo = arquivo_temporario.read_text()
    assert "Jogador 1 venceu | 2x0 | Melhor de 3" in conteudo


def test_salvar_multiplas_partidas(arquivo_temporario):
    salvar_partida(1, 2, 1, 3)
    salvar_partida(2, 1, 3, 5)
    linhas = arquivo_temporario.read_text().strip().split("\n")
    assert len(linhas) == 2


def test_carregar_historico_vazio(arquivo_temporario):
    #arquivo existe mas está vazio
    assert carregar_historico() == []


def test_carregar_historico_sem_arquivo(monkeypatch, tmp_path):
    #arquivo não existe
    monkeypatch.setattr("src.dados.RANKING_PATH", str(tmp_path / "inexistente.txt"))
    assert carregar_historico() == []


def test_carregar_historico_ordem(arquivo_temporario):
    #deve retornar da mais recente para a mais antiga
    salvar_partida(1, 2, 0, 3)
    salvar_partida(2, 0, 2, 3)
    historico = carregar_historico()
    assert historico[0].startswith("Jogador 2")
    assert historico[1].startswith("Jogador 1")


def test_carregar_historico_limite(arquivo_temporario):
    #deve retornar no máximo 10 partidas
    for i in range(15):
        salvar_partida(1, 2, 0, 3)
    assert len(carregar_historico()) == 10
