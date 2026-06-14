import pygame
from pygame import gfxdraw

from src.config import bg_color, prop_color, ball_radius, player_width, player_height, ball_speed, player_speed, fps
from src.funcoes import inverter, bateu_em_cima_ou_embaixo, bateu_nas_laterais, limitar_jogador, bateu_no_jogador


def tela_selecao_modo(screen, screen_width, screen_height):
    font_title = pygame.font.Font(None, 100)
    font_button = pygame.font.Font(None, 50)
    font_info = pygame.font.Font(None, 40)
    
    # Criar botões
    button_width, button_height = 300, 100
    button_spacing = 100
    
    button_3_x = (screen_width // 2) - button_width - (button_spacing // 2)
    button_5_x = (screen_width // 2) + (button_spacing // 2)
    button_y = (screen_height - button_height) // 2
    
    button_3_rect = pygame.Rect(button_3_x, button_y, button_width, button_height)
    button_5_rect = pygame.Rect(button_5_x, button_y, button_width, button_height)
    
    selecionado = None
    menu_ativo = True
    
    while menu_ativo:
        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_3_rect.collidepoint(mouse_pos):
                    selecionado = 3
                    menu_ativo = False
                elif button_5_rect.collidepoint(mouse_pos):
                    selecionado = 5
                    menu_ativo = False
        
        # Desenhar tela de seleção
        screen.fill(bg_color)
        
        # Título
        title_text = font_title.render("PONG", True, prop_color)
        title_rect = title_text.get_rect(center=(screen_width//2, 150))
        screen.blit(title_text, title_rect)
        
        # Subtítulo
        subtitle_text = font_info.render("Escolha o modo de jogo", True, prop_color)
        subtitle_rect = subtitle_text.get_rect(center=(screen_width//2, 300))
        screen.blit(subtitle_text, subtitle_rect)
        
        # Botão Melhor de 3
        button_3_color = pygame.Color("#ff6b6b") if button_3_rect.collidepoint(mouse_pos) else prop_color
        pygame.draw.rect(screen, button_3_color, button_3_rect)
        pygame.draw.rect(screen, prop_color, button_3_rect, 3)
        button_3_text = font_button.render("Melhor de 3", True, bg_color)
        button_3_text_rect = button_3_text.get_rect(center=button_3_rect.center)
        screen.blit(button_3_text, button_3_text_rect)
        
        # Botão Melhor de 5
        button_5_color = pygame.Color("#ff6b6b") if button_5_rect.collidepoint(mouse_pos) else prop_color
        pygame.draw.rect(screen, button_5_color, button_5_rect)
        pygame.draw.rect(screen, prop_color, button_5_rect, 3)
        button_5_text = font_button.render("Melhor de 5", True, bg_color)
        button_5_text_rect = button_5_text.get_rect(center=button_5_rect.center)
        screen.blit(button_5_text, button_5_text_rect)
        
        pygame.display.update()
    
    return selecionado

#Exibe a tela de resultado final da série
def tela_resultado_final(screen, screen_width, screen_height, vencedor):
    font_title = pygame.font.Font(None, 150)
    font_info = pygame.font.Font(None, 80)
    
    clock = pygame.time.Clock()
    contador = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return
        
        # Desenhar tela de resultado
        screen.fill(bg_color)
        
        # Título
        title_text = font_title.render("FIM DE JOGO", True, prop_color)
        title_rect = title_text.get_rect(center=(screen_width//2, 300))
        screen.blit(title_text, title_rect)
        
        # Vencedor
        vencedor_text = font_info.render(f"Jogador {vencedor} venceu!", True, pygame.Color("#ff6b6b"))
        vencedor_rect = vencedor_text.get_rect(center=(screen_width//2, 500))
        screen.blit(vencedor_text, vencedor_rect)
        
        pygame.display.update()
        clock.tick(fps)
        contador += 1
        
        # Encerrar automaticamente após 3 segundos (180 frames a 60 FPS)
        if contador >= 180:
            return


def run():
    pygame.init()
    #tamanho da janela do app
    display_info = pygame.display.Info()
    screen_width, screen_height = display_info.current_w, display_info.current_h
    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

    # Exibir tela de seleção de modo
    modo = tela_selecao_modo(screen, screen_width, screen_height)
    
    # Calcular limite de vitórias baseado no modo
    vitoria_limite = 2 if modo == 3 else 3
    
    score_p1 = 0
    score_p2 = 0

    #posicionamento inicial da bola, player1 e player2
    ball = pygame.Rect(screen_width//2-ball_radius, screen_height//2-ball_radius, ball_radius*2, ball_radius*2)
    player1 = pygame.Rect(0, screen_height//2-player_height//2, player_width, player_height)
    player2 = pygame.Rect(screen_width-player_width, screen_height//2-player_height//2, player_width, player_height)

    #velocidade da bola
    ball_speed_x, ball_speed_y = ball_speed, ball_speed
    player1_delta, player2_delta = 0, 0

    #fonte para exibir pontuação
    font = pygame.font.Font(None, 74)

    clock = pygame.time.Clock()

    pausa_frames = 4

    while score_p1 < vitoria_limite and score_p2 < vitoria_limite:
        #cria a forma de fechar o app
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            #configurando o comando de decer os player com as teclas S e SetaParaBaixo
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return
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

        # Se não está em pausa, continua jogando
        if pausa_frames == 0:
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
            
            if ball.left <= 0:
                score_p2 += 1
                ball.x = screen_width//2-ball_radius
                ball.y = screen_height//2-ball_radius
                ball_speed_x = ball_speed
                ball_speed_y = ball_speed
            elif ball.right >= screen_width:
                score_p1 += 1
                ball.x = screen_width//2-ball_radius
                ball.y = screen_height//2-ball_radius
                ball_speed_x = -ball_speed
                ball_speed_y = ball_speed
            else:
                if bateu_nas_laterais(ball.left, ball.right, screen_width):
                    ball_speed_x = inverter(ball_speed_x)

            if bateu_no_jogador(ball, player1) and ball_speed_x < 0:
                ball_speed_x = inverter(ball_speed_x)
            elif bateu_no_jogador(ball, player2) and ball_speed_x > 0:
                ball_speed_x = inverter(ball_speed_x)
        else:
            pausa_frames -= 1

        #cria a linha que divide os campos e o desenho do circulo
        screen.fill(bg_color)
        pygame.draw.aaline(screen, prop_color, (screen_width//2, 0), (screen_width//2, screen_height))
        gfxdraw.aacircle(screen, screen_width//2, screen_height//2, 200, prop_color)
        pygame.draw.rect(screen, prop_color, player1)
        pygame.draw.rect(screen, prop_color, player2)
        gfxdraw.filled_circle(screen, ball.centerx, ball.centery, ball_radius, prop_color)
        
        # Exibir pontuação da partida na tela
        score_text = font.render(f"{score_p1}  {score_p2}", True, prop_color)
        score_rect = score_text.get_rect(center=(screen_width//2, 100))
        screen.blit(score_text, score_rect)
        
        pygame.display.update()
        clock.tick(fps)
    
    vencedor = 1 if score_p1 >= vitoria_limite else 2
    tela_resultado_final(screen, screen_width, screen_height, vencedor)
    pygame.quit()