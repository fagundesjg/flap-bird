import os

import pygame

from src.configs import GRAVITY, GAME_SPEED, SCREEN_SIZE


class Bird(pygame.sprite.Sprite):
    def __init__(self, color, size):
        pygame.sprite.Sprite.__init__(self)
        self.started = False
        self.gravity = GRAVITY
        self.game_speed = GAME_SPEED
        self.size = size
        self.color = color
        self.current_image = 0
        self.images = list(map(lambda img: pygame.transform.scale(pygame.image.load(os.path.join(
            "src", "assets", "sprites", self.color + img)).convert_alpha(), self.size), ["bird-downflap.png", "bird-midflap.png", "bird-upflap.png"]))
        self.image = self.images[self.current_image]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.bump_sound = pygame.mixer.Sound(os.path.join(
            "src", "assets", "audio", "wing.wav"))

    def bump(self):
        self.game_speed -= int(SCREEN_SIZE[1] / 50)
        self.bump_sound.play()
        if self.game_speed < -int(SCREEN_SIZE[1] / 30):
            self.game_speed = -int(SCREEN_SIZE[1] / 30)

    def start(self):
        self.started = True

    def update(self):
        self.current_image = (self.current_image + 1) % len(self.images)
        self.image = self.images[self.current_image]
        if self.started:
            self.game_speed += self.gravity
            self.rect[1] += self.game_speed
