from typing import Counter
from aocd import data, lines, numbers, submit
import numpy as np
import re
import sys
from aoc_utils import intify, neigh4, neigh8

rocks="""####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##""".split("\n\n")

rocks = [
    [[1,1,1,1]],
    [[0,1,0],[1,1,1], [0,1,0]],
    [[1,1,1], [0,0,1], [0,0,1]],
    [[1],[1],[1],[1],],
    [[1,1], [1,1]],
]
rocks = [np.array(r, dtype=int) for r in rocks]

dat = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"
shifts = [-1 if c=='<' else 1 for c in data]
len_shifts = len(shifts)
W=7
R=5
NN=1000000000000
N=len_shifts*R
f = np.zeros((1000000, W), dtype=int)
rx=0
jetx=0
lev = 0

def check(rock, pos):
    if pos[1]<0 or pos[1]+rock.shape[1]>W:
        return False
    h,w = rock.shape
    if pos[0]<0: return False
    if (f[pos[0]:pos[0]+h, pos[1]:pos[1]+w]*rock).sum()!=0:
        return False
    return True

def show():
    if lev<20:
        a = f[:lev, :]
    else:
        a = f[lev-20:lev, :]
    for l in np.flip(a,axis=0):
        print("".join(l.astype(str)))
    print()

istart = 1785
levstart = 2778
di399 = 1720
dlev399 = 2729
iend = (NN-istart)%di399
levoffset = ((NN-istart)//di399)*dlev399
for i in range(istart+iend):
    # if rx==0:
    #     if jetx==399:
    #         print(i, lev, i-i399, lev-lev399)
    #         i399=i
    #         lev399=lev
    rock = rocks[rx]
    rx = (rx+1)%R
    pos = np.array([lev+3, 2], dtype=int)
    while True:
        new = pos + [0, shifts[jetx]]
        jetx = (jetx+1)%len_shifts
        if check(rock, new):
            pos = new
        new = pos - [1, 0]
        if check(rock, new):
            pos = new
        else:
            f[pos[0]:pos[0]+rock.shape[0], pos[1]:pos[1]+rock.shape[1]] += rock
            lev = max(lev, pos[0]+rock.shape[0])
            break

submit(lev+levoffset)