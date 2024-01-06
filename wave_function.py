from data import *
from drawing_function import *
import pygame

# init pygame
pygame.init()

# create screen with size window
screen = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()

# auto display
while True:
    # check wether QUIT event occures
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    generate_background()
    bg = pygame.image.load('images/background.png')

    # put the background into the screen
    screen.blit(bg, (0, 0))

    # setting FPS
    clock.tick(FPS)

    # display
    pygame.display.update()
