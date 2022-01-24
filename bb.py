from gg import start
from main import game
from pvp import pvp
from dffghf import red
from tt import write_level, lvl
from plaerm import men
from pvpend import pvp_end


stand = 1
mp1, mp2, level, score, win, winner = None, None, None, None, None, None
while stand != 0:
    if stand == 1:  #гл меню
        stand = start()
    elif stand == 2:  # 1инра
        stand, score, level, win = game(mp1, mp2, level)
    elif stand == 3:  #два инра
        stand, winner = pvp()
    elif stand == 4:  #три игра
        stand, m1, m2 = red()
        write_level(m1, m2)
    elif stand == 5: #выбор уровня
        stand, mp1, mp2, level = lvl()
    elif stand == 6: #завершени1 1 игра
        stand, mp1, mp2 = men(score, level, win)
    elif stand == 7: #завершени2 2 игра
        stand = pvp_end(winner)