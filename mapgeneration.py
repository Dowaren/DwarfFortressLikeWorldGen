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
                        
    return map
