
import msvcrt
import os

from colorama import Fore
from perlin_noise import PerlinNoise

noise = PerlinNoise(octaves=6, seed=4522)
amp = 6
period = 24

width = 440
widthw = 190
heightw = 250

map = []

for i in range(heightw):
    os.system("cls")
    map.append([])

    if i % 2 == 0:
        print(f"Loading / | {i}/{heightw}")
    elif i % 3 == 0:
        print(f"Loading - | {i}/{heightw}")
    else:
        print(f"Loading \\| {i}/{heightw}")
    for j in range(width):
        height = (noise([i / 30, j / 120]) * 20)
        if round(height) == 0:
            map[i].append((Fore.BLUE + "≃"))
        elif round(height) == -1:
            map[i].append(Fore.YELLOW + "⋛")
        elif round(height) < -2 and round(height) != -3 and round(height) != -10:
            map[i].append(Fore.GREEN + "↥")
        elif round(height) == 1:
            map[i].append((Fore.BLUE + "≃"))
        elif round(height) > 2:
            map[i].append((Fore.BLUE + "≃"))
        elif round(height) == -3:
            map[i].append(Fore.WHITE + '▲')
        elif round(height) == -10:
            map[i].append(Fore.WHITE + '⋒')

x = widthw

offsetx = 0
offsety = 0
while True:
    os.system("cls")

    str = ""

    for i in range(29):
        for j in range(120):
            str += map[i + offsety][offsetx + j]

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

    if a == b"e":
        exit(0)
