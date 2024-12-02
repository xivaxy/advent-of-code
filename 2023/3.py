from aocd import data, submit
from aocd.models import Puzzle
import numpy as np
import string
import re
import sys
from aoc_utils import intify, neigh4, neigh8

ans = 0 

s="""467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592-....
......755.
...$.*....
.664.598.."""

non_symbols = ".0123456789"
gear_symbol = "*"
lines = data.split("\n")
w = len(lines[0])
gear_locations = {}
for i in range(len(lines)):
    for j in range(w):
        if lines[i][j] == gear_symbol:
            gear_locations[(i, j)] = []

for i in range(len(lines)):
    start = None
    for j in range(w):
        if lines[i][j] in string.digits:
            if start is None:
                start = j
        elif start is not None:
            end = j
            num = int(lines[i][start:end])
            nbrs = [(i, start-1), (i, end)]
            if i>0:
                nbrs.extend([(i-1, x) for x in range(start-1, end+1)])
            if i<len(lines)-1:
                nbrs.extend([(i+1, x) for x in range(start-1, end+1)])
            for x,y in nbrs:
                if (x,y) in gear_locations:
                    gear_locations[(x,y)].append(num)
            start = None

    if start is not None:
        end = w
        num = int(lines[i][start:end])
        nbrs = [(i, start-1), (i, end)]
        if i>0:
            nbrs.extend([(i-1, x) for x in range(start-1, end+1)])
        if i<len(lines)-1:
            nbrs.extend([(i+1, x) for x in range(start-1, end+1)])
        for x,y in nbrs:
            if (x,y) in gear_locations:
                gear_locations[(x,y)].append(num)

for x,y in gear_locations:
    if len(gear_locations[(x,y)]) == 2:
        ans += np.prod(gear_locations[(x,y)])
# print(gear_locations)
print(ans)
submit(ans)