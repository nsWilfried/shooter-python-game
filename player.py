import pygame
from projectile import Projectile
# build player

class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super(Player, self).__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.velocity = 3
        self.image = pygame.image.load('assets/assets/player.png')
        self.attack = 10
        self.rect = self.image.get_rect()
        self.rect.x = 240
        self.rect.y = 280
        self.all_left_projectiles = pygame.sprite.Group()
        self.all_right_projectiles = pygame.sprite.Group()

    def move_left(self):
        self.rect.x -= self.velocity

    def move_right(self):
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def launch_left_projectile(self, x, y):
        self.all_left_projectiles.add(Projectile(self, x, y, self.game))

    def launch_right_projectile(self, x, y):
        self.all_right_projectiles.add(Projectile(self, x, y, self.game))

    def health_bar(self, surface):
        pygame.draw.rect(surface, (0, 0, 0), [self.rect.x + 50, self.rect.y - 20, self.max_health, 8])
        pygame.draw.rect(surface, (22, 232, 22), [self.rect.x + 50, self.rect.y - 20, self.health, 8])

    def damage(self, monster):
        self.health -= monster.attack

        if self.health <= 0:
            self.game.is_playing = False

