from aocd import data, submit
from aocd.models import Puzzle
import numpy as np
import re, sys
from aoc_utils import intify, neigh4, neigh8

# tags: area inside 2d contour, geometry, shoelace/trapezoid formula

ans=0
s='''R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)'''
# data=s
# #70c710 -> 0x70c71 distance and 0 direction
# directions 0 means R, 1 means D, 2 means L, and 3 means U
direction_map = {'0': (1, 0), '1': (0, -1), '2': (-1, 0), '3': (0, 1)}
a = [ (direction_map[x[-2]], int(x[-7:-2], 16)) for x in data.split('\n') ]

# direction_map = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}
# a = [ (direction_map[x.split()[0]], int(x.split()[1])) for x in data.split('\n') ]
perimeter = 0
x = 0
y=0
for (dx, dy), d in a:
    perimeter += d
    ans+=x*dy*d
    x+=dx*d
    y+=dy*d

ans = abs(ans+x*(0-y)) + perimeter//2+1

print(ans)
submit(ans)