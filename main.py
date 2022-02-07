# coding=utf-8
import pygame
from game import Game

pygame.init()
game = Game()

# on initialise les modules de pygame
pygame.display.set_caption("Shooter game")
screen = pygame.display.set_mode((1080, 540))
background = pygame.image.load('assets/assets/bg.jpg')
running = True


#  la boucle du jeu
while running:

    # pour appliquer le background
    screen.blit(background, (0, -440))

    if game.is_playing == True:
        game.load_game(screen)
    else:
        game.banner_rect.x = screen.get_width()/4
        game.playing_button_rect.x = screen.get_width()/3 - 30
        game.playing_button_rect.y = screen.get_height()/2 +70
        screen.blit(game.playing_button, game.playing_button_rect)
        screen.blit(game.banner, game.banner_rect)

    # mettre à jour la fenêtre
    pygame.display.flip()
    # verifier si le user compte aller a gauche ou  a droite
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < 920:
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            if event.key == pygame.K_SPACE:
                game.player.launch_right_projectile(120, 90)

            elif event.key == pygame.K_BACKSPACE:
                game.player.launch_left_projectile(0, 90)

        elif event.type == pygame.KEYUP:
                game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if game.playing_button_rect.collidepoint(event.pos):
                game.is_playing = True
                game.player.health = game.player.max_health

