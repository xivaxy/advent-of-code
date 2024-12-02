from aocd import data, submit
from aocd.models import Puzzle
import numpy as np
import re, sys
from aoc_utils import intify, neigh4, neigh8

ans=0
s='''0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45'''
# data=s
for line in data.splitlines():
    nums=intify(line.split())
    nums = np.array(nums).reshape(-1)
    # print(nums)
    diffs = []
    for i in range(0, len(nums)-1):
        diffs.append(np.diff(nums, i))
        if np.all(diffs[-1] == 0):
            break
    # compute the next number of nums
    # print(diffs)
    r = 0
    for df in diffs[::-1]:
        r = df[0]-r
    # print(diffs)
    # print(r)
    ans+=r
    

print(ans)
submit(ans)