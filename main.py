import eventkeyhandler
import mapgeneration
import fragment
import msvcrt
offsetx = 0
offsety = 0
offsetz = 0

def start(offsetz,offsety,offsetx):
    map = mapgeneration.mapgen()
    update(map, offsetz,offsety,offsetx)
def update(map, offsetz,offsety,offsetx):
    while True:
        fragment.render(map, offsetz, offsetx, offsety)

        listvecs = eventkeyhandler.getevent(msvcrt.getch(), [offsetz,offsety,offsetx])
        offsetx = listvecs[2]
        offsetz = listvecs[0]
        offsety = listvecs[1]


start(offsetz,offsety,offsetx)
