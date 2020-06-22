import os

import pygame


class Pipe(pygame.sprite.Sprite):
    def __init__(self, color, game_speed, size, pos, inverted=False):
        pygame.sprite.Sprite.__init__(self)
        self.color = color
        self.size = size
        self.pos = pos
        self.inverted = inverted
        self.started = False
        self.game_speed = game_speed
        self.image_name = "pipe-" + self.color
        self.image_name += "-inverted.png" if self.inverted else ".png"
        self.image = pygame.transform.scale(pygame.image.load(os.path.join(
            "src", "assets", "sprites", self.image_name)).convert_alpha(), self.size)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect[0] = pos[0]
        self.rect[1] = pos[1]
        self.added_score = False

    def update(self):
        self.rect[0] -= self.game_speed
