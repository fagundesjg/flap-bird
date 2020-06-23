import os
import sys

import pygame
from pygame.locals import QUIT, K_SPACE, KEYDOWN
from random import randint

from src.bird import Bird
from src.ground import Ground
from src.pipe import Pipe
from src.score import Score
from src.configs import SCREEN, SOUNDS, IMAGES, SCREEN_SIZE, GAME_SPEED, GRAVITY, FPS, BIRD_SIZE


class App():
    def __init__(self):
        self.running = True
        self.started = False
        self.gravity = GRAVITY
        self.clock = pygame.time.Clock()
        self.schedule = 0
        self.bird = Bird()
        self.score = 0
        self.bird_group = pygame.sprite.Group()
        self.ground_group = pygame.sprite.Group()
        self.pipe_group = pygame.sprite.Group()
        self.score_group = pygame.sprite.Group()
        self.__add_bird()
        self.__add_ground()
        self.__render_score()
        self.change_schedule()  # troca o dia pela noite

    def add_score(self):
        self.score += 1
        self.__render_score()
        SOUNDS["POINT"].play()

    def generate_pipe(self):
        pipe_height = int(SCREEN_SIZE[1] / 2)
        offset = randint(0, int(SCREEN_SIZE[1] / 3))
        for i in range(2):
            offset *= 1 if i == 1 else -1
            pos_y = i * (SCREEN_SIZE[1] - int(SCREEN_SIZE[1] / 4)) + offset
            pipe = Pipe(color="green", game_speed=GAME_SPEED,
                        size=(int(SCREEN_SIZE[0] / 6), pipe_height), pos=(SCREEN_SIZE[0], pos_y), inverted=not bool(i))
            self.pipe_group.add(pipe)

    def change_schedule(self):
        self.schedule = (self.schedule + 1) % 2

    def __add_bird(self):
        # Responsável por fazer o passaro aparecer no centro da tela
        self.bird.rect[0] = SCREEN_SIZE[0] / 2 - BIRD_SIZE[0] / 2
        self.bird.rect[1] = SCREEN_SIZE[1] / 2 - BIRD_SIZE[1] / 2
        self.bird_group.add(self.bird)

    def __add_ground(self):
        height = int(SCREEN_SIZE[1] / 8)
        ground = Ground(size=(SCREEN_SIZE[0] * 2, height),
                        pos=(0, SCREEN_SIZE[1] - height),
                        game_speed=GAME_SPEED)
        self.ground_group.add(ground)

    def __render_score(self):
        for sprite in self.score_group.sprites():
            self.score_group.remove(sprite)
        i = 0
        score_points = f"{self.score}"
        spacing = SCREEN_SIZE[1] / 24
        size = len(score_points)
        margin_left = int((SCREEN_SIZE[0] / 2) -
                          (size * spacing + size * 2) / 2)
        for num in score_points:
            score = Score(num=num, pos=(
                margin_left + (i * (spacing + 2)), SCREEN_SIZE[1] / 10))
            self.score_group.add(score)
            i += 1

    def __x_is_off_screen(self, sprite):
        return sprite.rect[0] < -(sprite.rect[2])

    def __y_is_off_screen(self, sprite):
        return sprite.rect[1] < -(sprite.rect[3])

    def handle_pipes(self):
        for sprite in self.pipe_group.sprites():
            if sprite.rect[0] < int(SCREEN_SIZE[0] / 2.7) and len(self.pipe_group.sprites()) <= 2:
                self.generate_pipe()
                self.add_score()
            if self.__x_is_off_screen(sprite):
                self.pipe_group.remove(sprite)

    def handle_events(self):
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
            self.running = False
        if(pygame.sprite.groupcollide(self.bird_group, self.pipe_group, False, False, pygame.sprite.collide_mask)):
            SOUNDS["HIT"].play()
            self.running = False

    def update(self):
        SCREEN.blit(IMAGES["BACKGROUNDS"][self.schedule], (0, 0))

        self.handle_pipes()
        self.bird_group.update()
        self.pipe_group.update()
        self.ground_group.update()
        self.score_group.update()

        self.bird_group.draw(SCREEN)
        self.pipe_group.draw(SCREEN)
        self.ground_group.draw(SCREEN)
        self.score_group.draw(SCREEN)

        pygame.display.update()

    def start(self):
        while self.running:
            self.clock.tick(FPS)
            self.handle_events()
            self.update()
        print(">> Game over!")
