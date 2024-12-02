from aocd import data, submit
from aocd.models import Puzzle
import numpy as np
import re, sys
from aoc_utils import intify, neigh4, neigh8

ans=0
s='''O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....'''
# data=s
# . = 0, # = 1, O = 2
a = np.array([[0 if c=='.' else 1 if c=='#' else 2 for c in l] for l in data.split('\n')])
h,w = a.shape
num_cycles = 1000000000

def cycle():
    global a,h,w
    for k in range(4):
        # slide all the round rocks O up until the edge or the next square rock #
        for j in range(w):
            s = -1  # current pointer
            for i in range(h):
                if a[i,j]==0 and s==-1:
                    s = i
                elif a[i,j]==1:
                    s=-1
                elif a[i,j]==2:
                    if s!=-1:
                        a[s,j]=2
                        a[i,j]=0
                        s+=1
        # rotate a clockwise
        a[:] = a[::-1].T
        h,w = w,h


weights = np.arange(h, 0, -1, dtype=int).reshape(h, 1)
scores = []
visited = dict()
window = 7
while True:
    cycle()
    score = np.sum((a==2)*weights)
    scores.append(score)
    if len(scores)>window:
        key = tuple(scores[-window:])
        if key in visited:
            print("Cycle start", visited[key]-window)
            print("Cycle start 2", len(scores)-window)
            period = len(scores)-visited[key]
            offset = visited[key]-window
            # value at num_cycles
            ans = scores[(num_cycles-visited[key])%period+visited[key]-1]
            break
        else:
            visited[key] = len(scores)
        

print(ans)
# submit(ans)