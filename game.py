# coding=utf-8
import pygame
from monser import Monster
from player import Player
from comet import Comet
from comet_event import CometEvent

class Game:
    def __init__(self):
        self.player = Player(self)
        self.all_monsters = pygame.sprite.Group()
        self.build_monster()
        self.build_monster()
        self.pressed = {}
        self.is_playing = False
        self.banner = pygame.image.load('assets/assets/banner.png')
        self.banner = pygame.transform.scale(self.banner, (500, 500))
        self.banner_rect = self.banner.get_rect()
        self.playing_button = pygame.image.load('assets/assets/button.png')
        self.playing_button = pygame.transform.scale(self.playing_button, (400, 200))
        self.playing_button_rect = self.playing_button.get_rect()
        self.comet_event = CometEvent()
        self.all_comets = pygame.sprite.Group()

    def start(self):
        self.is_playing = True

    def load_game(self, screen):

        # afficher l'image du joueur
        screen.blit(self.player.image, self.player.rect)
        self.comet_event.build_bar(screen)
        self.comet_event.move_bar()

        # si la barre de pourcentage est au max, on affiche les comets
        if self.comet_event.percent >= 1080:
            self.comet_event.percent = 0
            self.all_comets.add(Comet(self))


        # faire bouger la comet
        for comet in self.all_comets:
            comet.move_comet()

            # Si la comète dépasse l"écran alors on la supprime
            if comet.rect.y >= screen.get_height():
                self.all_comets.remove(comet)

        # faire bouger le projectile gauche
        for left_projectile in self.player.all_left_projectiles:
            left_projectile.move_projectile_left()

        # faire bouger le projectile droit
        for right_projectile in self.player.all_right_projectiles:
            right_projectile.move_projectile_right()

        # faire bouger !le monstre et afficher leur barre de vie
        for monster in self.all_monsters:
            monster.move_monster()
            monster.build_health_bar(screen)

        # afficher les projectiles, les monstres, la barre de vie du joueur
        self.player.all_left_projectiles.draw(screen)
        self.player.all_right_projectiles.draw(screen)
        self.all_monsters.draw(screen)
        self.player.health_bar(screen)
        self.all_comets.draw(screen)




    def build_monster(self):
        self.all_monsters.add(Monster(self))

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)