import os

import pygame


class Ground(pygame.sprite.Sprite):
    def __init__(self, size, pos, game_speed):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.pos = pos
        self.image = pygame.transform.scale(pygame.image.load(os.path.join(
            "src", "assets", "sprites", "base.png")).convert(), self.size)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.game_speed = game_speed
        self.rect[0] = self.pos[0]
        self.rect[1] = self.pos[1]
        self.x = 0

    def update(self):
        self.rect[0] -= self.game_speed
        self.x += self.game_speed
        if self.x >= int(self.size[0] / 2):
            self.rect[0] = 0
            self.x = 0
