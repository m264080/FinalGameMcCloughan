import pygame
import sys
import random
from bigmeat import Bigmeat, bigmeats
from badbird import Badbird, badbirds
from zza import Zza
from game_parameters import *
from utilities import draw_background, add_meat, add_badbirds, add_shrooms
from shroomshooter import shrooms
from menu_screen import display_menu
from math import cos, sin, atan2


#initialize pygame
pygame.init()


#create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Using tiles and blit to draw on surface")

clock = pygame.time.Clock()

background = screen.copy()
draw_background(background)

add_meat(10)
add_badbirds(1)
zza = Zza(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

#initialize score with custom font
score = 0
score_font = pygame.font.Font("../assets-finalgame/fonts/Black_Crayon.ttf", 48)

life_icon = pygame.image.load("../assets-finalgame/sprites/lives.png").convert()
life_icon = pygame.transform.flip(life_icon, True, False)
life_icon.set_colorkey((255, 255, 255))

life_icon = pygame.transform.scale(life_icon, (50, 50))
lives = NUM_LIVES

pygame.mixer.music.load("../assets-finalgame/song.mp3")
pygame.mixer_music.play(-1) #carmen showed me how to do this

pygame.mixer.init()
hurtsound = pygame.mixer.Sound("../assets-finalgame/soundahhh.mp3")

meatcounter = 0

for _ in range(5):
    bigmeats.add(Bigmeat(random.randint(0, SCREEN_WIDTH-TILE_SIZE), 0))


# def loadhighscore():
#     try:
#         with open("highscore.txt", "r") as file:
#             return int(file.read())
#     except FileNotFoundError:
#         return 0
#
# def savehighscore():
#     with open("highscore.txt", "w") as file:
#         file.write(str(score))
# highscore = loadhighscore()

restart = True


#bigmeatcounter = 3
#gameover = len(bigmeats) < 0 or lives <0
#main - actually runs the code
running = True
space_pressed = True  # waiting for user to press space bar
while running and lives >0 and len(bigmeats) > 0:############################### run while there are big meats left
    while space_pressed:
        display_menu(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                space_pressed = False  # once the space bar is pressed, = false so function ends --> game begins

    # if len(bigmeats) <2 and bigmeatcounter >0:
    #     add_meat(3)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        # control player with arrow keys
        zza.stop()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                    zza.move_up()
            if event.key == pygame.K_LEFT:
                    zza.move_left()
            if event.key == pygame.K_RIGHT:
                    zza.move_right()
            if event.key == pygame.K_DOWN:
                    zza.move_down()
            # if event.key == pygame.K_SPACE:
            #     pos = zza.rect.midright
            #     add_shrooms(1, pos, angle)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                    #player.x, player.y = pygame.mouse.get_pos()

                    #pos = player.rect.midright
                mouse_x, mouse_y = pygame.mouse.get_pos()
                angle = - atan2(mouse_y - zza.y, mouse_x - zza.x)
                add_shrooms(1, zza.rect.center, angle)

    #draws background
    screen.blit(background, (0,0))

    zza_x, zza_y = zza.rect.center
    for bird in badbirds:
        bird_x, bird_y = bird.rect.center
        direction = atan2(zza_y - bird_y, zza_x - bird_x)
        bird.update(direction)

    #update the sprites
    bigmeats.update()
    #badbirds.update(5)
    zza.update()
    shrooms.update(zza)

    result = pygame.sprite.spritecollide(zza, bigmeats, True) #checks for collisions between the sprites
    if result:
        score += len(result)
        # play hurt sound
        #pygame.mixer.Sound.play("../final game/assets-finalgame/soundahhh.mp3")
        # add new meat
        add_meat(len(result))
        meatcounter = meatcounter + 1
        bigmeats.add(Bigmeat(random.randint(0, SCREEN_WIDTH - TILE_SIZE), 0))

    result2 = pygame.sprite.spritecollide(zza, badbirds, True)#check for collisions
    if result2:
        lives -= len(result2)
        # play chomp sound
        #pygame.mixer.Sound.play(chomp)
        # add new fish
        hurtsound.play()
        add_badbirds(len(result2))
        bigmeats.add(Bigmeat(random.randint(0, SCREEN_WIDTH - TILE_SIZE), 0))

    # Remove off-screen bigmeats, idk chat gpt helped me with this
    bigmeats = pygame.sprite.Group([bigmeat for bigmeat in bigmeats if bigmeat.rect.top < SCREEN_HEIGHT])
    # if len(bigmeats) < 5:
    #     bigmeats.add(Bigmeat(random.randint(0, SCREEN_WIDTH - TILE_SIZE), 0))
    #


    bigmeats.draw(screen)
    zza.draw(screen)
    badbirds.draw(screen)##############


    for bigmeat in bigmeats:
        if bigmeat.rect.y < -bigmeat.rect.height:
            bigmeats.remove(zza)
            add_meat(1)
    for badbird in badbirds:
        if badbird.rect.y < -badbird.rect.height:
            badbirds.remove(badbird)
            add_badbirds(1)

    for shroom in shrooms:
        if shroom.rect.x > SCREEN_WIDTH:
            shrooms.remove(shroom)

        for badbird in badbirds:
            shroom_enemy = pygame.sprite.spritecollide(shroom, badbirds, True)
            if shroom_enemy:
                score += len(shroom_enemy)
                badbirds.remove(badbird)
                add_badbirds(1)
                shrooms.remove(shroom)


        for bigmeat in bigmeats:
            shroom_fish = pygame.sprite.spritecollide(shroom, bigmeats, True)
            if shroom_fish:
                score -= len(shroom_fish)
                bigmeats.remove(bigmeat)
                add_meat(1)
                shrooms.remove(shroom)
############################################################################

    # for bigmeat in bigmeats:
    #     if bigmeat.rect.x < -zza.rect.width:
    #         bigmeats.remove(zza)
    #         bigmeats.add(Bigmeat(random.randint(SCREEN_WIDTH, SCREEN_WIDTH*2), random.randint(TILE_SIZE, SCREEN_HEIGHT-TILE_SIZE)))

    # for bigmeat in bigmeats:
    #     if bigmeat.rect.y < -bigmeat.rect.height:
    #         bigmeats.remove(bigmeat)
    #         bigmeats.add(Bigmeat(random.randint(0, SCREEN_WIDTH - TILE_SIZE), 0))
    #         #bigmeats.add(Bigmeat(random.randint(SCREEN_WIDTH, SCREEN_WIDTH*2), random.randint(TILE_SIZE, SCREEN_HEIGHT-TILE_SIZE)))



    for shroom in shrooms:
        shroom.draw_shroom(screen)

    text = score_font.render(f"{score}", True, (255, 0, 0))
    screen.blit(text, (SCREEN_WIDTH - text.get_width() - 10, 0))

    #draws num of lives left:
    for i in range(lives):
        screen.blit(life_icon, (i*TILE_SIZE, SCREEN_HEIGHT-TILE_SIZE))

    # if gameover:
    #     display_menu(screen)

    # if score > highscore:
    #     highscore = score
    #     savehighscore(highscore)#writes highscore into the file


    #update the display
    pygame.display.flip()


    clock.tick(60)

#chat gpt help with the following code:
#game over screen will show after running loop ends
screen.fill((0, 0, 0))
big_font = pygame.font.Font("../assets-finalgame/fonts/From_Cartoon_Blocks.ttf", 124)
small_font = pygame.font.Font("../assets-finalgame/fonts/VertigoFLF-Bold.ttf", 24)
youdie_text = big_font.render("you die", True, (220,208,255))
screen.blit(youdie_text, (SCREEN_WIDTH // 2 - youdie_text.get_width() // 2,
                              SCREEN_HEIGHT // 2 - youdie_text.get_height() // 2))
restart_text = small_font.render("press 'r' to exit (u suck)", True, (255, 255, 255))
screen.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2,
                            SCREEN_HEIGHT // 2 + youdie_text.get_height() // 2))
# score_text = game_over_font.render("high score: " +str(highscore), True, (255, 255, 255))
# screen.blit(score_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2,
#                             SCREEN_HEIGHT // 2 + game_over_text.get_height()+restart_text.get_height() // 2))


pygame.display.flip()

restart = True
while restart:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r: #once r is pressed, game will replay
            add_meat(10)
            lives = NUM_LIVES
            score = 0
            space_pressed = True
            restart = False

#quit game
pygame.quit()
sys.exit()


