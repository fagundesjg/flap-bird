import os
import sys

import pygame
from pygame.locals import QUIT, K_SPACE, KEYDOWN
from random import randint

from src.bird import Bird
from src.ground import Ground
from src.pipe import Pipe
from src.score import Score


class App():
    def __init__(self):
        pygame.init()
        self.size = (300, 600)
        self.started = False
        self.game_speed = 5
        self.gravity = 1
        self.clock = pygame.time.Clock()
        self.backgrounds = [pygame.transform.scale(pygame.image.load(os.path.join(
            "src", "assets", "sprites", "background-day.png")), self.size), pygame.transform.scale(pygame.image.load(os.path.join("src", "assets", "sprites", "background-night.png")), self.size)]
        self.screen = pygame.display.set_mode(self.size)
        self.bird = Bird(color="yellow", size=(30, 25), gravity=self.gravity)
        self.score = 0
        self.bird_group = pygame.sprite.Group()
        self.ground_group = pygame.sprite.Group()
        self.pipe_group = pygame.sprite.Group()
        self.score_group = pygame.sprite.Group()
        self.__add_bird()
        self.__add_ground()
        self.__render_score()
        self.die_sound = pygame.mixer.Sound(os.path.join(
            "src", "assets", "audio", "die.wav"))
        self.hit_sound = pygame.mixer.Sound(os.path.join(
            "src", "assets", "audio", "hit.wav"))
        self.point_sound = pygame.mixer.Sound(os.path.join(
            "src", "assets", "audio", "point.wav"))

    def add_score(self):
        self.score += 1
        self.__render_score()
        self.point_sound.play()

    def generate_pipe(self):
        pipe_height = int(self.size[1] / 2)
        offset = randint(0, 200)
        for i in range(2):
            offset *= 1 if i == 1 else -1
            pos_y = i * (self.size[1] - 150) + offset
            pipe = Pipe(color="green", game_speed=self.game_speed,
                        size=(50, pipe_height), pos=(self.size[0], pos_y), inverted=not bool(i))
            self.pipe_group.add(pipe)

    def __add_bird(self):
        self.bird.rect[0] = self.size[0] / 2 - 15
        self.bird.rect[1] = self.size[1] / 2 - 12.5
        self.bird_group.add(self.bird)

    def __add_ground(self):
        height = int(self.size[1] / 8)
        ground = Ground(size=(self.size[0] * 2, height),
                        pos=(0, self.size[1] - height),
                        game_speed=self.game_speed)
        self.ground_group.add(ground)

    def __render_score(self):
        for sprite in self.score_group.sprites():
            self.score_group.remove(sprite)
        i = 0
        score_points = f"{self.score}"
        margin_left = int((self.size[0] / 2) - (len(score_points) * 27) / 2)
        for num in score_points:
            score = Score(num=num, pos=(margin_left + (i*27), 60))
            self.score_group.add(score)
            i += 1

    def __x_is_off_screen(self, sprite):
        return sprite.rect[0] < -(sprite.rect[2])

    def __y_is_off_screen(self, sprite):
        return sprite.rect[1] < -(sprite.rect[3])

    def handle_pipes(self):
        for sprite in self.pipe_group.sprites():
            if sprite.rect[0] < int(self.size[0] / 4) and len(self.pipe_group.sprites()) <= 2:
                self.generate_pipe()
                self.add_score()
            if self.__x_is_off_screen(sprite):
                self.pipe_group.remove(sprite)

    def update(self):
        self.screen.blit(self.backgrounds[0], (0, 0))

        self.handle_pipes()
        self.bird_group.update()
        self.pipe_group.update()
        self.ground_group.update()
        self.score_group.update()

        self.bird_group.draw(self.screen)
        self.pipe_group.draw(self.screen)
        self.ground_group.draw(self.screen)
        self.score_group.draw(self.screen)

        pygame.display.update()

    def start(self):
        running = True
        while running:
            self.clock.tick(30)
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()

                if event.type == KEYDOWN:
                    if self.started:
                        if event.key == K_SPACE and not self.__y_is_off_screen(self.bird_group.sprites()[0]):
                            self.bird.bump()
                    if not self.started:
                        if event.key == K_SPACE:
                            self.started = True
                            self.bird.start()
                            self.generate_pipe()

            if (pygame.sprite.groupcollide(self.bird_group, self.ground_group, False, False, pygame.sprite.collide_mask)):
                running = False
            if(pygame.sprite.groupcollide(self.bird_group, self.pipe_group, False, False, pygame.sprite.collide_mask)):
                self.hit_sound.play()
                running = False

            self.update()

        print(">> Game over!")
