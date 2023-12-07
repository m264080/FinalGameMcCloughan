import pygame
import sys
import random
import time
from game_parameters import *
from utilities import draw_background, add_meat
#from main import screen


def display_menu(screen):
    background = screen.copy()
    draw_background(background)#draws the background with dimentions from the screen


    # load game font
    big_font = pygame.font.Font("../assets-finalgame/fonts/From_Cartoon_Blocks.ttf", 128)
    small_font = pygame.font.Font("../assets-finalgame/fonts/VertigoFLF-Bold.ttf", 48)
    micro_font = pygame.font.Font("../assets-finalgame/fonts/VertigoFLF-Bold.ttf", 24)


    #create text object with the message "chomp" to display, and tuple (253, 69, 0) as font color
    text = big_font.render("PIZZA", True, (0, 0, 0))
    smaller_text = small_font.render("Press SPACE to play!", True, (0, 0, 0))
    micro_text1 = micro_font.render("1. Collect ALL the meats", True, (0, 0, 0))
    micro_text2 = micro_font.render("2. Shoot down the bird", True, (0, 0, 0))


    # draws background
    screen.blit(background, (0, 0))

    # draw text at center of display
    screen.blit(text, (SCREEN_WIDTH / 2 - text.get_width() / 2, SCREEN_HEIGHT / 2 - text.get_height() / 2 - 75))
    screen.blit(smaller_text, (SCREEN_WIDTH / 2 - text.get_width() / 2 +40, SCREEN_HEIGHT / 2 - text.get_height() / 2 + 120))
    screen.blit(micro_text1, (SCREEN_WIDTH / 2 - text.get_width() / 2 + 80, SCREEN_HEIGHT / 2 - text.get_height() / 2 + 175))
    screen.blit(micro_text2, (SCREEN_WIDTH / 2 - text.get_width() / 2 + 80, SCREEN_HEIGHT / 2 - text.get_height() / 2 + 200))


    pygame.display.flip()

    # space_pressed = True # waiting for user to press space bar
    # while space_pressed:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             pygame.quit()
    #             sys.exit()
    #         elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
    #             space_pressed = False # once the space bar is pressed, = false so function ends --> game begins


#
# pygame.display.set_caption("Using tiles and blit to draw on surface")

