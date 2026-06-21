import os
import json

#caminho para o arquivo de histórico de partidas
RANKING_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "ranking.json")


#salva o resultado da partida no arquivo de histórico
def salvar_partida(vencedor, score_p1, score_p2, modo):
    partidas = _ler_json()
    partidas.append({
        "vencedor": vencedor,
        "score_p1": score_p1,
        "score_p2": score_p2,
        "modo": modo
    })
    with open(RANKING_PATH, "w") as f:
        json.dump(partidas, f, indent=2)


#lê e retorna as últimas 10 partidas, da mais recente para a mais antiga
def carregar_historico():
    partidas = _ler_json()
    ultimas = partidas[-10:][::-1]
    return [f"Jogador {p['vencedor']} venceu | {p['score_p1']}x{p['score_p2']} | Melhor de {p['modo']}" for p in ultimas]


#apaga todo o histórico de partidas
def apagar_historico():
    with open(RANKING_PATH, "w") as f:
        json.dump([], f)


#lê o arquivo json e retorna a lista de partidas
def _ler_json():
    try:
        with open(RANKING_PATH, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
