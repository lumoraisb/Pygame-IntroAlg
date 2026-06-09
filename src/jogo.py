import pygame
from pygame import gfxdraw

from src.config import bg_color, prop_color, ball_radius, player_width, player_height, ball_speed, player_speed, fps
from src.funcoes import inverter, bateu_em_cima_ou_embaixo, bateu_nas_laterais, limitar_jogador, bateu_no_jogador


def run():
    pygame.init()
    #tamanho da janela do app
    display_info = pygame.display.Info()
    screen_width, screen_height = display_info.current_w, display_info.current_h
    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

    #posicionamento inicial da bola, player1 e player2
    ball = pygame.Rect(screen_width//2-ball_radius, screen_height//2-ball_radius, ball_radius*2, ball_radius*2)
    player1 = pygame.Rect(0, screen_height//2-player_height//2, player_width, player_height)
    player2 = pygame.Rect(screen_width-player_width, screen_height//2-player_height//2, player_width, player_height)

    #velocidade da bola
    ball_speed_x, ball_speed_y = ball_speed, ball_speed
    player1_delta, player2_delta = 0, 0

    clock = pygame.time.Clock()

    while True:
        #cria a forma de fechar o app
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            #configurando o comando de decer os player com as teclas S e SetaParaBaixo
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_s:
                    player1_delta = player_speed
                if event.key == pygame.K_w:
                    player1_delta = -player_speed
                if event.key == pygame.K_DOWN:
                    player2_delta = player_speed
                if event.key == pygame.K_UP:
                    player2_delta = -player_speed
            #configurando o comando de subir os player com as teclas W e SetaParacima
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_s or event.key == pygame.K_w:
                    player1_delta = 0
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    player2_delta = 0

        player1.y += player1_delta
        player2.y += player2_delta

        #limite que o player pode subir ou decer
        limitar_jogador(player1, screen_height)
        limitar_jogador(player2, screen_height)

        ball.x += ball_speed_x
        ball.y += ball_speed_y

        #Quando a bola bater em alguma extremidade ela ricocheteia 
        if bateu_em_cima_ou_embaixo(ball.top, ball.bottom, screen_height):
            ball_speed_y = inverter(ball_speed_y)
        if bateu_nas_laterais(ball.left, ball.right, screen_width):
            ball_speed_x = inverter(ball_speed_x)

        if bateu_no_jogador(ball, player1) or bateu_no_jogador(ball, player2):
            ball_speed_x = inverter(ball_speed_x)

        #cria a linha que divide os campos e o desenho do circulo
        screen.fill(bg_color)
        pygame.draw.aaline(screen, prop_color, (screen_width//2, 0), (screen_width//2, screen_height))
        gfxdraw.aacircle(screen, screen_width//2, screen_height//2, 200, prop_color)
        pygame.draw.rect(screen, prop_color, player1)
        pygame.draw.rect(screen, prop_color, player2)
        gfxdraw.filled_circle(screen, ball.centerx, ball.centery, ball_radius, prop_color)
        pygame.display.update()
        clock.tick(fps)