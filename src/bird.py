import os

import pygame


class Bird(pygame.sprite.Sprite):
    def __init__(self, color, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.color = color
        self.current_image = 0
        self.images = list(map(lambda img: pygame.transform.scale(pygame.image.load(os.path.join(
            "src", "assets", "sprites", self.color + img)).convert_alpha(), self.size), ["bird-downflap.png", "bird-midflap.png", "bird-upflap.png"]))
        self.image = self.images[self.current_image]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()

    def update(self):
        self.current_image = (self.current_image + 1) % len(self.images)
        self.image = self.images[self.current_image]
