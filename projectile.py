import pygame
class Projectile(pygame.sprite.Sprite):
    def __init__(self, player, x, y, game):
        super(Projectile, self).__init__()
        self.game = game
        self.velocity = 2
        self.player = player
        self.image = pygame.image.load('assets/assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.rect.x = self.player.rect.x + x
        self.rect.y = self.player.rect.y + y
        self.originalImage = self.image
        self.angle = 30

    def rotate_projectile(self):
        self.image = pygame.transform.rotozoom(self.originalImage, self.angle,1)

    def move_projectile_right(self):
        self.rect.x += self.velocity
        self.rotate_projectile()

        if self.rect.x > 920 or self.game.check_collision(self, self.game.all_monsters):
            self.player.all_right_projectiles.remove(self)
            for monster in self.game.check_collision(self, self.game.all_monsters):
                monster.damage(self)
                if monster.health == 0:
                    monster.rect.x = 900
                    monster.health = monster.max_health

    def move_projectile_left(self):
        self.rect.x -= self.velocity
        self.rotate_projectile()

        if self.rect.x <= 0 :
            self.player.all_left_projectiles.remove(self)
