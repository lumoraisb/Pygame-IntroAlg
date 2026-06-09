#funcoes do jogo

def inverter(velocidade):
    return velocidade * -1


def bateu_em_cima_ou_embaixo(topo, base, altura_tela):
    if topo <= 0 or base >= altura_tela:
        return True
    return False


def bateu_nas_laterais(esquerda, direita, largura_tela):
    if esquerda <= 0 or direita >= largura_tela:
        return True
    return False


def limitar_jogador(jogador, altura_tela):
    if jogador.top < 0:
        jogador.top = 0
    if jogador.bottom > altura_tela:
        jogador.bottom = altura_tela
    return jogador


def bateu_no_jogador(bola, jogador):
    return bola.colliderect(jogador)