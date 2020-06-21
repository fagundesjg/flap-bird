import os

import pygame


class Ground(pygame.sprite.Sprite):
    def __init__(self, size, game_speed):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = pygame.transform.scale(pygame.image.load(os.path.join(
            "src", "assets", "sprites", "base.png")).convert_alpha(), self.size)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.game_speed = game_speed

    def update(self):
        self.rect[0] -= self.game_speed
