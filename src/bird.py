import os

import pygame


class Bird(pygame.sprite.Sprite):
    def __init__(self, color, size, gravity):
        pygame.sprite.Sprite.__init__(self)
        self.gravity = gravity
        self.speed = 5
        self.size = size
        self.color = color
        self.current_image = 0
        self.images = list(map(lambda img: pygame.transform.scale(pygame.image.load(os.path.join(
            "src", "assets", "sprites", self.color + img)).convert_alpha(), self.size), ["bird-downflap.png", "bird-midflap.png", "bird-upflap.png"]))
        self.image = self.images[self.current_image]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()

    def bump(self):
        self.speed -= 12
        if self.speed < -20:
            self.speed = -20

    def update(self):
        self.current_image = (self.current_image + 1) % len(self.images)
        self.image = self.images[self.current_image]
        self.speed += self.gravity
        self.rect[1] += self.speed
