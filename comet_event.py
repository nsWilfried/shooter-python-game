import pygame

class CometEvent:

    def __init__(self):
        self.percent = 0
        self.max_percent = 100
        self.velocity = 5

    def build_bar(self, surface):
        pygame.draw.rect(surface, (0, 0, 0), [0, surface.get_height() - 25, surface.get_width(), 25])
        pygame.draw.rect(surface, (65, 48, 84),  [0, surface.get_height() - 25, self.percent, 25])

    def move_bar(self):
        self.percent += self.velocity

        if self.percent == 100:
            print('total')

