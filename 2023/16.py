from aocd import data, submit
from aocd.models import Puzzle
import numpy as np
import re, sys
from aoc_utils import intify, neigh4, neigh8

ans=0
s=r'''.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....'''
# data=s
a = data.splitlines()
h,w = len(a), len(a[0])
# tuples are (x,y, direction in neigh4)

def add(x,y,d):
    x+=neigh4[d][0]
    y+=neigh4[d][1]
    if 0<=x<h and 0<=y<w:
        return (x,y,d)
    else:
        return None
slash_dir_map = {0:1, 1:0, 2:3, 3:2}
backslash_dir_map = {0:3, 1:2, 2:1, 3:0}
b = [list(l) for l in a]
# b[0][0] = '*'
# print('\n'.join(''.join(l) for l in b))
for start in [(x,0,3) for x in range(h)] + [(0,y,0) for y in range(w)] + [(x,w-1,1) for x in range(h)] + [(h-1,y,2) for y in range(w)]:
    rays = [start]
    visited = set(rays)
    while rays:
        x,y,d = rays.pop()
        nxts = []
        match (a[x][y]):
            case '|':
                if d in [1,3]:
                    for d in [0,2]:
                        nxts.append(add(x,y,d))
                else:
                    nxts.append(add(x,y,d))
            case '-':
                if d in [0,2]:
                    for d in [1,3]:
                        nxts.append(add(x,y,d))
                else:
                    nxts.append(add(x,y,d))
            case '/':
                nxts.append(add(x,y,slash_dir_map[d]))
            case '\\':
                nxts.append(add(x,y,backslash_dir_map[d]))
            case _:
                nxts.append(add(x,y,d))
        for nxt in nxts:
            if nxt and nxt not in visited:
                visited.add(nxt)
                rays.append(nxt)
                # b[nxt[0]][nxt[1]] = '*'
                # print('\n'.join(''.join(l) for l in b))

    ans  = max(ans, len({(x,y) for x,y,d in visited}))

print(ans)
submit(ans)