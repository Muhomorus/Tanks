from gg import start
from main import game


stand = 1
while stand != 0:
    if stand == 1:
        stand = start()
    elif stand == 2:
        stand = game()