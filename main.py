import pygame
from player import Player
from monser import Monster

pygame.init()


class Game:
    def __init__(self):
        self.player = Player(self)
        self.all_monsters = pygame.sprite.Group()
        self.build_monster()
        self.pressed = {}

    def build_monster(self):
        self.all_monsters.add(Monster(self))

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)


game = Game()
# on initialise les modules de pygame
pygame.display.set_caption("Shooter game")
screen = pygame.display.set_mode((1080, 540))
background = pygame.image.load('assets/assets/bg.jpg')
running = True
#  la boucle du jeu
while running:



    # pour appliquer le background
    screen.blit(background, (0,-440))
    screen.blit(game.player.image, game.player.rect)


    for left_projectile in game.player.all_left_projectiles:
        left_projectile.move_projectile_left()

    for right_projectile in game.player.all_right_projectiles:
        right_projectile.move_projectile_right()

    for monster in game.all_monsters:
        monster.move_monster()
        monster.build_health_bar(screen)

    game.player.all_left_projectiles.draw(screen)
    game.player.all_right_projectiles.draw(screen)
    game.all_monsters.draw(screen)
    game.player.health_bar(screen)

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
