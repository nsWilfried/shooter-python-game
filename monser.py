import pygame
import random

class Monster(pygame.sprite.Sprite):
    def __init__(self, game):
        super(Monster, self).__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.1
        self.velocity = random.randint(1, 2)
        self.image = pygame.image.load('assets/assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 800 + random.randint(1,300)
        self.rect.y = 320

    def move_monster(self):
        if not self.game.check_collision(self.game.player, self.game.all_monsters):
            if self.rect.x >= 0:
                self.rect.x -= self.velocity
        else:
            self.game.player.damage(self)

    def build_health_bar(self, surface):
        bar_color = (22, 232, 22)
        bar_total = (0,0,0)
        bar_dimension = [self.rect.x, self.rect.y, self.health, 5]
        bar_dimension_total = [self.rect.x, self.rect.y, self.max_health, 5]
        pygame.draw.rect(surface, bar_total, bar_dimension_total)
        pygame.draw.rect(surface, bar_color, bar_dimension)

    def damage(self, player):
        self.health -= player.player.attack