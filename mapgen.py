import os
import random

from tqdm import tqdm
from config import *
from colorama import Fore
from perlin_noise import PerlinNoise
import opensimplex

opensimplex.seed(4522)
opensimplex.random_seed()
noise = PerlinNoise(octaves=6, seed=random.randrange(1000,9999))

map = []

def mapgen():
    for z in tqdm (range(depthofworld),
               desc="Map Generating",
               ascii=False, ncols=75):
        opensimplex.random_seed()
        map.append([])
        for i in range(heightw):

            map[z].append([])

            if z == 0:
                for j in range(widthw):
                    height = (noise([i / 30, j / 120]) * 20)
                    if round(height) == 0:
                        map[z][i].append(("W"))
                    elif round(height) == -1:
                        map[z][i].append("S")
                    elif round(height) < -2 and round(height) != -3 and round(height) != -10:
                        map[z][i].append("F")
                    elif round(height) == 1:
                        map[z][i].append(("W"))
                    elif round(height) > 2:
                        map[z][i].append(("W"))
                    elif round(height) == -3:
                        map[z][i].append('M')
                    elif round(height) == -10:
                        map[z][i].append('H')

            else:
                for j in range(width):
                    height = opensimplex.noise2(x=i, y=j) * 20
                    if round(height) < 0:
                        map[z][i].append(" ")
                    else:
                        map[z][i].append("#")
    return map