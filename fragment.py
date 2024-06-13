import os


listtorender = []


def render(map, offsetz, offsetx, offsety):
    os.system("cls")
    listtorender = []
    str = ""
    listtorender = map.copy()

    for i in range(29):
        for j in range(120):
            str += listtorender[offsetz][i + offsety][offsetx + j]
    print(str)
