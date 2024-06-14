
import random
import mapgen
from config import *
import pygame
import pygame.image

pygame.init()

map = mapgen.mapgen()

screen = pygame.display.set_mode([1280, 720])


#you can replace images to load tile set. Asset res is 10x10
image = pygame.image.load('assets/water.png').convert_alpha()
forest = pygame.image.load('assets/forest.png').convert_alpha()
house = pygame.image.load('assets/house.png').convert_alpha()
mountain = pygame.image.load('assets/mountain.png').convert_alpha()
sand = pygame.image.load('assets/sand.png')
cavewall = pygame.image.load('assets/sand.png')

offsetx = 0
offsety = 0
offsetz = 0

running = True
print(map)


while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False


    keys = pygame.key.get_pressed()



    if keys[pygame.K_a] and offsety > -1:
        print(offsety)
        offsety -= 1
    elif keys[pygame.K_d] and offsety < 160:
        print(offsety)
        offsety += 1
    elif keys[pygame.K_s] and offsetx < 160:
        print(offsetx)
        offsetx += 1
    elif keys[pygame.K_w] and offsetx > -1:
        print(offsetx)
        offsetx -= 1

    elif keys[pygame.K_x] and offsetz < depthofworld - 2:
        print(offsetz)
        offsetz += 1

    elif keys[pygame.K_z] and offsetz - 1 > - 1:
        print(offsetz)
        offsetz -= 1
    screen.fill((0, 0, 0))




    for i in range(128):
        for j in range(72):
            if map[offsetz][offsetx + j][i + offsety] == "W":
                screen.blit(image, (i*10, j*10))
            elif map[offsetz][offsetx + j][i + offsety] == "F":
                screen.blit(forest, (i*10, j*10))
            elif map[offsetz][offsetx + j][i + offsety] == "M":
                screen.blit(mountain, (i*10, j*10))
            elif map[offsetz][offsetx + j][i + offsety] == "H":
                screen.blit(house, (i*10, j*10))
            elif map[offsetz][offsetx + j][i + offsety] == "S":
                screen.blit(sand, (i*10, j*10))
            elif map[offsetz][offsetx + j][i + offsety] == "#":
                screen.blit(cavewall, (i * 10, j * 10))
            elif map[offsetz][offsetx + j][i + offsety] == " ":
                pass






    pygame.display.flip()




pygame.quit()
