from config import *


def getevent(a, curvec3offfsets):
    offsetx = curvec3offfsets[2]
    offsety = curvec3offfsets[1]
    offsetz = curvec3offfsets[0]

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

    return [offsetz, offsety, offsetx]
