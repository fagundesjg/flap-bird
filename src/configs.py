import pygame
import os


SCREEN_WIDTH = 400
SCREEN_HEIGHT = 700
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

GAME_SPEED = int(SCREEN_WIDTH / 60)
GRAVITY = 1 * (SCREEN_HEIGHT / 600)
FPS = 30

BIRD_SIZE = (int(SCREEN_SIZE[0] / 10), int(SCREEN_SIZE[1] / 24))

pygame.init()
SCREEN = pygame.display.set_mode(SCREEN_SIZE)

SOUNDS = {
    "DIE": pygame.mixer.Sound(os.path.join(
        "src", "assets", "audio", "die.wav")),
    "HIT": pygame.mixer.Sound(os.path.join(
        "src", "assets", "audio", "hit.wav")),
    "POINT": pygame.mixer.Sound(os.path.join(
        "src", "assets", "audio", "point.wav")),
    "BUMP": pygame.mixer.Sound(os.path.join(
        "src", "assets", "audio", "wing.wav"))
}
IMAGES = {
    "BACKGROUNDS": [pygame.transform.scale(pygame.image.load(os.path.join(
        "src", "assets", "sprites", "background-day.png")), SCREEN_SIZE), pygame.transform.scale(pygame.image.load(os.path.join("src", "assets", "sprites", "background-night.png")), SCREEN_SIZE)],
    "BIRDS": list(map(lambda color: tuple(map(lambda img: pygame.transform.scale(pygame.image.load(os.path.join(
        "src", "assets", "sprites", color + img)).convert_alpha(), BIRD_SIZE), ["bird-downflap.png", "bird-midflap.png", "bird-upflap.png"])), ["red", "yellow", "blue"]))
}
