from aocd import data, submit
from aocd.models import Puzzle
import numpy as np
import re, sys
from aoc_utils import intify, neigh4, neigh8

ans=1
s='''Time:      7  15   30
Distance:  9  40  200'''
# data=s

lines = data.splitlines()
times = int("".join([x for x in lines[0].split()[1:]]))
distances = int("".join([x for x in lines[1].split()[1:]]))
for i in range(1):
    ways = 0
    for j in range(1, times):
        speed = j
        dist = speed * (times-j)
        if dist > distances:
            ways+=1
    ans *= ways

print(ans)
submit(ans)