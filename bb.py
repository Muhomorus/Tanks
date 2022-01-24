from gg import start
from main import game
from pvp import pvp
from dffghf import red
from tt import write_level, lvl


stand = 1
mp1, mp2 = None, None
while stand != 0:
    if stand == 1:
        stand = start()
    elif stand == 2:
        stand = game(mp1, mp2)
    elif stand == 3:
        stand = pvp()
    elif stand == 4:
        stand, m1, m2 = red()
        write_level(m1, m2)
    elif stand == 5:
        stand, mp1, mp2 = lvl()