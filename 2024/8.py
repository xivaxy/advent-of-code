from aocd import data, submit
import sys
sys.path.append('../advent-of-code')
from aoc_utils import intify, neigh4, neigh8
import re
# import numpy as np
# import regex as re
# from z3 import *

s='''............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............'''
test = False
if test:
    data=s
ans=0
lines = data.split('\n')
m,n = len(lines), len(lines[0])
locs = dict()
for i in range(m):
    for j in range(n):
        if lines[i][j] != '.':
            frequency = lines[i][j]
            if frequency not in locs:
                locs[frequency] = []
            locs[frequency].append((i,j))
# print(len(locs), locs)
nodes = set()
for f in locs:
    for i in range(len(locs[f])):
        for j in range(i+1, len(locs[f])):
            x1,y1 = locs[f][i]
            x2,y2 = locs[f][j]
            dx, dy = x2-x1, y2-y1
            for k in range(50):
                x,y = x1+k*dx, y1+k*dy
                if 0<=x<m and 0<=y<n:
                    nodes.add((x,y))
                else:
                    break
            for k in range(0, -50, -1):
                x,y = x1+k*dx, y1+k*dy
                if 0<=x<m and 0<=y<n:
                    nodes.add((x,y))
                else:
                    break

ans = len(nodes)

print(ans)
if not test:
    submit(ans)