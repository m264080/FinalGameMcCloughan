import pygame
from game_parameters import*
from math import cos, sin
import random

class Shroom (pygame.sprite.Sprite):
    def __init__(self, x, y, angle):
        super().__init__()

        shroompic = pygame.image.load("../assets-finalgame/sprites/shroompic.png").convert()
        shroompic = pygame.transform.flip(shroompic, True, False)
        shroompic.set_colorkey((255, 255, 255))

        self.image = pygame.transform.scale(shroompic, (25, 25))

        # # self.speed = random.uniform(BADBIRD_MIN_SPEED, BADBIRD_MAX_SPEED)

        #self.rect = pygame.Rect(0,0, SHROOM_WIDTH, SHROOM_HEIGHT)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.angle = angle

    def update(self, player):
        self.x += SHROOM_SPEED * cos(self.angle)
        self.y -= SHROOM_SPEED * sin(self.angle)
        self.rect.x, self.rect.y = self.x, self.y

    def draw_shroom(self, screen):
        screen.blit(self.image, self.rect)

shrooms = pygame.sprite.Group()

