import pygame

from src.funcoes import inverter, bateu_em_cima_ou_embaixo, bateu_nas_laterais, limitar_jogador, bateu_no_jogador


def test_inverter():
    assert inverter(5) == -5
    assert inverter(-5) == 5


def test_limitar_jogador():
    altura_tela = 600

    cima = pygame.Rect(0, -40, 10, 150)
    limitar_jogador(cima, altura_tela)
    assert cima.top == 0

    baixo = pygame.Rect(0, 700, 10, 150)
    limitar_jogador(baixo, altura_tela)
    assert baixo.bottom == altura_tela


def test_bateu_no_jogador():
    jogador = pygame.Rect(0, 100, 10, 150)
    encostando = pygame.Rect(5, 150, 30, 30)
    longe = pygame.Rect(400, 150, 30, 30)
    assert bateu_no_jogador(encostando, jogador) == True
    assert bateu_no_jogador(longe, jogador) == False


def test_bateu_nas_bordas():
    largura_tela, altura_tela = 800, 600
    assert bateu_em_cima_ou_embaixo(0, 30, altura_tela) == True
    assert bateu_em_cima_ou_embaixo(100, 130, altura_tela) == False
    assert bateu_nas_laterais(0, 30, largura_tela) == True
    assert bateu_nas_laterais(100, 130, largura_tela) == False