import os

#caminho para o arquivo de histórico de partidas
RANKING_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "ranking.txt")


#salva o resultado da partida no arquivo de histórico
def salvar_partida(vencedor, score_p1, score_p2, modo):
    with open(RANKING_PATH, "a") as f:
        f.write(f"Jogador {vencedor} venceu | {score_p1}x{score_p2} | Melhor de {modo}\n")


#lê e retorna as últimas 10 partidas, da mais recente para a mais antiga
def carregar_historico():
    try:
        with open(RANKING_PATH, "r") as f:
            linhas = f.readlines()
    except FileNotFoundError:
        return []
    return [l.strip() for l in linhas if l.strip()][-10:][::-1]
