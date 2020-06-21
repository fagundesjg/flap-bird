import os
import sys

import pygame

from src.bird import Bird
from src.ground import Ground


class App():
    def __init__(self):
        pygame.init()
        self.size = (300, 600)
        self.game_speed = 7
        self.clock = pygame.time.Clock()
        self.backgrounds = [pygame.transform.scale(pygame.image.load(os.path.join(
            "src", "assets", "sprites", "background-day.png")), self.size), pygame.transform.scale(pygame.image.load(os.path.join("src", "assets", "sprites", "background-night.png")), self.size)]
        self.screen = pygame.display.set_mode(self.size)
        self.bird_group = pygame.sprite.Group()
        self.ground_group = pygame.sprite.Group()
        self.__add_bird()
        self.__add_ground(height=self.size[1] / 8)

    def __add_bird(self):
        bird = Bird(color="red", size=(30, 25))
        bird.rect[0] = self.size[0] / 2 - 15
        bird.rect[1] = self.size[1] / 2 - 12.5
        self.bird_group.add(bird)

    def __add_ground(self, height):
        height = int(height)
        for i in range(2):
            ground = Ground(size=(self.size[0], height),
                            game_speed=self.game_speed)
            ground.rect[0] = i * self.size[0]
            ground.rect[1] = self.size[1] - height
            self.ground_group.add(ground)

    def __x_is_off_screen(self, sprite):
        return sprite.rect[0] < -(sprite.rect[2])

    def __handle_ground_loop(self):
        if self.__x_is_off_screen(sprite=self.ground_group.sprites()[0]):
            height = int(self.size[1] / 8)
            self.ground_group.remove(self.ground_group.sprites()[0])
            ground = Ground(size=(self.size[0], height),
                            game_speed=self.game_speed)
            ground.rect[0] = self.size[0] - 25
            ground.rect[1] = self.size[1] - height
            self.ground_group.add(ground)

    def update(self):
        self.screen.blit(self.backgrounds[0], (0, 0))

        self.bird_group.update()
        self.ground_group.update()
        self.__handle_ground_loop()

        self.bird_group.draw(self.screen)
        self.ground_group.draw(self.screen)

        pygame.display.update()

    def start(self):
        while True:
            self.clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.update()
