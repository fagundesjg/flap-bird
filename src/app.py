import os
import sys

import pygame


class App():
    def __init__(self):
        pygame.init()
        self.size = (300, 600)
        self.clock = pygame.time.Clock()
        self.backgrounds = [pygame.transform.scale(pygame.image.load(os.path.join(
            "src", "assets", "sprites", "background-day.png")), self.size), pygame.transform.scale(pygame.image.load(os.path.join("src", "assets", "sprites", "background-night.png")), self.size)]
        self.screen = pygame.display.set_mode(self.size)

    def update(self):
        self.screen.blit(self.backgrounds[0], (0, 0))
        pygame.display.update()

    def start(self):
        while True:
            self.clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.update()
