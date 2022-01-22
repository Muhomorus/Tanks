from gg import start
from main import game
from pvp import pvp
from dffghf import red


stand = 1
while stand != 0:
    if stand == 1:
        stand = start()
    elif stand == 2:
        stand = game()
    elif stand == 3:
        stand = pvp()
    elif stand == 4:
        stand, m1, m2 = red()