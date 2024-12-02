from aocd import data, submit
from aocd.models import Puzzle
import numpy as np
import re, sys, bisect
from aoc_utils import intify, neigh4, neigh8

ans=0
s='''...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....'''
# data=s
mul = 1000000
# create a 0-1 numpy array
a=np.array([[1 if c=='#' else 0 for c in line] for line in data.splitlines()])
# find locations of all ones
ones=np.argwhere(a==1)
# find all columns without a one
cols_without_ones=np.argwhere(np.sum(a,axis=0)==0).reshape(-1)
cols_without_ones.sort()
rows_without_ones=np.argwhere(np.sum(a,axis=1)==0).reshape(-1)
rows_without_ones.sort()
print(cols_without_ones, rows_without_ones)
# print(ones)
for i, (x,y) in enumerate(ones):
    for j in range(i+1, len(ones)):
        x2,y2=ones[j]
        dist=abs(x-x2)+abs(y-y2)
        i1, i2 = bisect.bisect_left(rows_without_ones, x), bisect.bisect_left(rows_without_ones, x2)
        dist+=abs(i2-i1)*(mul-1)
        i1, i2 = bisect.bisect_left(cols_without_ones, y), bisect.bisect_left(cols_without_ones, y2)
        dist+=abs(i2-i1)*(mul-1)
        ans+=dist

print(ans)
submit(ans)