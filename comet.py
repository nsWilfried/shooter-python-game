import pygame
import random

class Comet(pygame.sprite.Sprite): 
    
    def __init__(self, game):
        super(Comet, self).__init__()
        self.game = game
        self.attack = 4
        self.velocity = 1
        self.image = pygame.image.load('assets/assets/comet.png')
        self.rect = self.image.get_rect()
        self.rect.x = 0 + random.randint(0, 1000)
        self.rect.y = 0

    def move_comet(self):
        self.rect.y = self.rect.y + self.velocity

        if self.game.check_collision(self.game.player, self.game.all_comets):
            self.game.player.health -= self.attack
            self.game.all_comets.remove(self)

