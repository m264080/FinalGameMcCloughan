import pygame
import random

MIN_SPEED = 0.5
MAX_SPEED = 3

class Bigmeat(pygame.sprite.Sprite):

    def __init__(self, x,y):
        super().__init__()

        bigmeatpic = pygame.image.load("../assets-finalgame/sprites/bigmeat.png").convert()
        bigmeatpic = pygame.transform.flip(bigmeatpic, True, False)
        bigmeatpic.set_colorkey((255,255,255))

        self.image = pygame.transform.scale(bigmeatpic, (50, 50))

        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x,y)

        self.speed = random.uniform(MIN_SPEED, MAX_SPEED)

    def update(self):
        self.y += self.speed
        self.rect.y = self.y

    def draw(self, screen):
        screen.blit(self.image, self.rect)


bigmeats = pygame.sprite.Group()