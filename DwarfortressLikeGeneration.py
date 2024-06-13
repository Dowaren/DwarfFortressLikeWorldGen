
import msvcrt
import os

from colorama import Fore
from perlin_noise import PerlinNoise
import opensimplex

opensimplex.seed(4522)
opensimplex.random_seed()
noise = PerlinNoise(octaves=6, seed=4522)
amp = 6
period = 24

width = 440
widthw = 190
heightw = 250
depthofworld = 5
map = []

for z in range(depthofworld):
    opensimplex.random_seed()
    map.append([])
    for i in range(heightw):
        os.system("cls")
        map[z].append([])

        if i % 2 == 0:
            print(f"Loading / | {i}/{heightw} and level {z}/{depthofworld}")
        elif i % 3 == 0:
            print(f"Loading - | {i}/{heightw} and level {z}/{depthofworld}")
        else:
            print(f"Loading \\| {i}/{heightw} and level {z}/{depthofworld}")

        if z == 0:
            for j in range(width):
                height = (noise([i / 30, j / 120]) * 20)
                if round(height) == 0:
                    map[z][i].append((Fore.BLUE + "≃"))
                elif round(height) == -1:
                    map[z][i].append(Fore.YELLOW + "⋛")
                elif round(height) < -2 and round(height) != -3 and round(height) != -10:
                    map[z][i].append(Fore.GREEN + "↥")
                elif round(height) == 1:
                    map[z][i].append((Fore.BLUE + "≃"))
                elif round(height) > 2:
                    map[z][i].append((Fore.BLUE + "≃"))
                elif round(height) == -3:
                    map[z][i].append(Fore.WHITE + '▲')
                elif round(height) == -10:
                    map[z][i].append(Fore.WHITE + '⋒')

        else:
            for j in range(width):
                height = opensimplex.noise2(x=i, y=j) * 20
                if round(height) < 0:
                    map[z][i].append(Fore.WHITE + " ")
                else:
                    map[z][i].append(Fore.WHITE + "#")

x = widthw

offsetx = 0
offsety = 0
offsetz = 0
while True:
    os.system("cls")

    str = ""

    for i in range(29):
        for j in range(120):
            str += map[offsetz][i + offsety][offsetx + j]

    print(str)

    a = msvcrt.getch()

    if a == b"d" and offsetx + 120 < widthw - 1:
        offsetx += 1

    if a == b"a" and offsetx > 1:
        offsetx -= 1

    if a == b"s" and offsety + 30 < heightw - 1:
        offsety += 1

    if a == b"w" and offsety > 1:
        offsety -= 1


    if a == b"z" and offsetz + 1 < depthofworld - 1:
        offsetz += 1

    if a == b"x" and offsetz - 1 > 0 - 1:
        offsetz -= 1

    if a == b"e":
        exit(0)
