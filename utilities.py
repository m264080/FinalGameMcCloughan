import pygame
import random
from bigmeat import bigmeats, Bigmeat
from badbird import badbirds, Badbird
from shroomshooter import shrooms, Shroom
from game_parameters import *

#load tiles from assets folder
def draw_background(screen):
    sky = pygame.image.load("../assets-finalgame/sprites/water.png").convert()
    grass = pygame.image.load("../assets-finalgame/sprites/seagrass.png").convert()
    #sets png background to transparent
    sky.set_colorkey((0,0,0))
    grass.set_colorkey((255,255,255))
    #fills the background with color sky
    for x in range(0, SCREEN_WIDTH, TILE_SIZE):
        for y in range(0, SCREEN_HEIGHT, TILE_SIZE):
            screen.blit(sky, (x,y))
    #makes the grassy bottom of the screen
    for x in range(0, SCREEN_WIDTH, TILE_SIZE):
        screen.blit(grass, (x,SCREEN_HEIGHT-TILE_SIZE))
        screen.blit(grass, (x+30, SCREEN_HEIGHT - TILE_SIZE))
        screen.blit(grass, (x+20, SCREEN_HEIGHT - TILE_SIZE+5))
        screen.blit(grass, (x+50, SCREEN_HEIGHT - TILE_SIZE))
    # load game font
    custom_font = pygame.font.Font("../assets-finalgame/fonts/From_Cartoon_Blocks.ttf", 48)
    # create text object with the message "catch the meats" to display, and tuple (253, 69, 0) as font color
    text = custom_font.render("yummy pizza", True, (0, 0, 0))
    screen.blit(text, (SCREEN_WIDTH / 2 - text.get_width()/2,0))

#places pizza in random places
def add_meat(num_meat):
    for _ in range(num_meat):
        bigmeats.add(Bigmeat(random.randint(SCREEN_WIDTH, SCREEN_WIDTH*2), random.randint(TILE_SIZE, SCREEN_HEIGHT-TILE_SIZE)))

# def add_badbirds(num_birdbirds):
#     for _ in range(num_birdbirds):
#         badbirds.add(Badbird(random.randint(SCREEN_WIDTH, SCREEN_WIDTH*2), random.randint(TILE_SIZE, SCREEN_HEIGHT-TILE_SIZE)))

def add_badbirds(num_birdbirds):
    for _ in range(num_birdbirds):
        badbirds.add(Badbird(random.randint(0, SCREEN_WIDTH - TILE_SIZE), 0)) # badbird will come from sky


def add_shrooms (num_shrooms, pos, angle):
    for _ in range(num_shrooms):
        shrooms.add(Shroom(pos[0], pos[1], angle))

