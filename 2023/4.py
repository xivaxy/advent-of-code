from aocd import data, submit
from aocd.models import Puzzle
import numpy as np
import re
import sys
from aoc_utils import intify, neigh4, neigh8
ans = 0
n = len(data.splitlines())
sizes = [1]*n
for i, line in enumerate(data.splitlines()):
    line = line.split(": ")[1]
    winning, mine = line.split("|")
    winning = winning.split()
    mine = mine.split()
    cross = set(winning).intersection(set(mine))
    nl = len(cross)
    for j in range(nl):
        sizes[i+j+1] += sizes[i]

ans = sum(sizes)
print(ans)
submit(ans)