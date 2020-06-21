import os
import sys

import pygame
from pygame.locals import K_SPACE, KEYDOWN, QUIT

from src.bird import Bird
from src.ground import Ground


class App():
    def __init__(self):
        pygame.init()
        self.size = (300, 600)
        self.game_speed = 7
        self.gravity = 1
        self.clock = pygame.time.Clock()
        self.backgrounds = [pygame.transform.scale(pygame.image.load(os.path.join(
            "src", "assets", "sprites", "background-day.png")), self.size), pygame.transform.scale(pygame.image.load(os.path.join("src", "assets", "sprites", "background-night.png")), self.size)]
        self.screen = pygame.display.set_mode(self.size)
        self.bird = Bird(color="yellow", size=(30, 25), gravity=self.gravity)
        self.bird_group = pygame.sprite.Group()
        self.ground_group = pygame.sprite.Group()
        self.__add_bird()
        self.__add_ground(height=self.size[1] / 8)

    def __add_bird(self):
        self.bird.rect[0] = self.size[0] / 2 - 15
        self.bird.rect[1] = self.size[1] / 2 - 12.5
        self.bird_group.add(self.bird)

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

    def __y_is_off_screen(self, sprite):
        return sprite.rect[1] < -(sprite.rect[3])

    def __handle_ground_loop(self):
        if self.__x_is_off_screen(sprite=self.ground_group.sprites()[0]):
            self.ground_group.remove(self.ground_group.sprites()[0])
            height = int(self.size[1] / 8)
            ground = Ground(size=(self.size[0], height),
                            game_speed=self.game_speed)
            ground.rect[0] = self.size[0] - 30
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
        running = True
        while running:
            self.clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == KEYDOWN:
                    if event.key == K_SPACE and not self.__y_is_off_screen(self.bird_group.sprites()[0]):
                        self.bird.bump()

            if (pygame.sprite.groupcollide(self.bird_group, self.ground_group, False, False, pygame.sprite.collide_mask)):
                running = False

            self.update()
        print(">> Game over!")
