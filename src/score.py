import os

import pygame


class Score(pygame.sprite.Sprite):
    def __init__(self, num, pos):
        pygame.sprite.Sprite.__init__(self)
        self.num = num
        self.pos = pos
        self.size = (25, 30)
        self.image = pygame.transform.scale(pygame.image.load(os.path.join(
            "src", "assets", "sprites", self.num + ".png")), self.size)
        self.rect = self.image.get_rect()
        self.rect[0] = self.pos[0]
        self.rect[1] = self.pos[1]

    def update(self):
        pass
