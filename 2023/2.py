from aocd import data, submit
from aocd.models import Puzzle
import numpy as np
import re
import sys
from aoc_utils import intify, neigh4, neigh8

s="""Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

ans = 0

max_red = 12
max_green = 13
max_blue= 14

for line in data.splitlines():
    game, sets = line.split(':')
    game_id = int(game.split()[1])
    sets = sets.split(';')
    red = green = blue = 0
    for s in sets:
        colors = s.split(',')
        for c in colors:
            cnt = int(c.split()[0])
            clr = c.split()[1]
            if clr == 'red':
                red = max(red, cnt)
            elif clr == 'green':
                green = max(green, cnt)
            elif clr == 'blue':
                blue = max(blue, cnt)
    power = red*green*blue
    ans+=power


print(ans)
submit(ans)