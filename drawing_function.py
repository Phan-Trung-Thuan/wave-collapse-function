from data import *
from color_function import *
import pygame

# DRAWING BACKGROUND
def generate_background():
    # init empty image
    image = pygame.Surface(WINDOW_SIZE)

    light_choice = [i * 20 for i in range(5)] # 0, 20, 40, 60, 80
    space = 5
    n = 10
    for _ in range(80):
            if random.random() < 0.5:
                color = darkerColor(MAIN_COLOR, random.choice(light_choice))
            else:
                color = lighterColor(MAIN_COLOR, random.choice(light_choice)) 
            
            x = random.randint(0, WINDOW_WIDTH)
            y = random.randint(0, WINDOW_HEIGHT)

            num_particle = random.randint(3, 8)

            for i in range(num_particle):
                pixels = pygame.PixelArray(image)
                pixels[x:x + n, y:y + n] = darkerColor(color, i * 40)
                del pixels

                if random.random() < 0.5:
                    x += n + space
                else:
                    y += n + space

    # save image
    pygame.image.save(image, 'images/background.png')

# DRAWING SHAPE
shape_color = lighterColor(MAIN_COLOR, 50)
background_color = darkerColor(MAIN_COLOR, 150)

def i_shape(w=100, h=100, color=(255, 255, 255), bg_color=(0, 0, 0), path='shape.png'):
    img = pygame.Surface((w, h))
    img.fill(bg_color)

    for i in range(35, 65):
        for j in range(100):
            img.set_at((i, j), color)

    pygame.image.save(img, path)

def plus_shape(w=100, h=100, color=(255, 255, 255), bg_color=(0, 0, 0), path='shape.png'):
    img = pygame.Surface((w, h))
    img.fill(bg_color)

    for i in range(35, 65):
        for j in range(100):
            img.set_at((i, j), color)

    for i in range(100):
        for j in range(35, 65):
            img.set_at((i, j), color)

    pygame.image.save(img, path)

def l_shape(w=100, h=100, color=(255, 255, 255), bg_color=(0, 0, 0), path='shape.png'):
    img = pygame.Surface((w, h))
    img.fill(bg_color)

    for i in range(35, 65):
        for j in range(65):
            img.set_at((i, j), color)

    for i in range(35, 100):
        for j in range(35, 65):
            img.set_at((i, j), color)

    pygame.image.save(img, path)

def t_shape(w=100, h=100, color=(255, 255, 255), bg_color=(0, 0, 0), path='shape.png'):
    img = pygame.Surface((w, h))
    img.fill(bg_color)

    for i in range(35, 65):
        for j in range(100):
            img.set_at((i, j), color)

    for i in range(35, 100):
        for j in range(35, 65):
            img.set_at((i, j), color)

    pygame.image.save(img, path)

# GENERATING IMAGE
generate_background()

filename = ['I_shape.png', 'Plus_shape.png', 'L_shape.png', 'T_shape.png']
list_function = [i_shape, plus_shape, l_shape, t_shape]

for i in range(len(list_function)):
    list_function[i](color=shape_color, bg_color=background_color, 
                     path='images/' + filename[i])
