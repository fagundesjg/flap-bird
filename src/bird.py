import os

import pygame

from src.configs import GRAVITY, GAME_SPEED, SCREEN_SIZE, IMAGES, SOUNDS


class Bird(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.started = False
        self.gravity = GRAVITY
        self.game_speed = GAME_SPEED
        self.current_color = 0
        self.current_image = 0
        self.images = IMAGES["BIRDS"][self.current_color]
        self.image = self.images[self.current_image]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()

    def bump(self):
        self.game_speed -= int(SCREEN_SIZE[1] / 30)
        SOUNDS["BUMP"].play()
        if self.game_speed < -int(SCREEN_SIZE[1] / 35):
            self.game_speed = -int(SCREEN_SIZE[1] / 35)
            print("< - ", self.game_speed)

    def start(self):
        self.started = True

    def update(self):
        self.current_image = (self.current_image + 1) % len(self.images)
        self.image = self.images[self.current_image]
        if self.started:
            self.game_speed += self.gravity
            self.rect[1] += self.game_speed
