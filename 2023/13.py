from aocd import data, submit
from aocd.models import Puzzle
import numpy as np
import re, sys
from aoc_utils import intify, neigh4, neigh8

ans=0
s='''#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#'''
# data=s
data=data.split('\n\n')
for d in data:
    # .->0, #->1
    a = np.array([[0 if c=='.' else 1 for c in l] for l in d.split('\n')])
    h,w = a.shape
    # find the axis of symmetry
    # check vertical axes
    for ax in range(1, w):
        s = min(ax, w-ax)
        if np.sum(a[:,ax-s:ax]!=a[:,ax:ax+s][:,::-1])==1:
            ans+=ax
            break
    else:
        # check horizontal axes
        for ax in range(1, h):
            s = min(ax, h-ax)
            if np.sum(a[ax-s:ax,:]!=a[ax:ax+s][::-1,:])==1:
                ans+=100*ax
                break

print(ans)
submit(ans)