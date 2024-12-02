from aocd import data, submit
from aocd.models import Puzzle
import numpy as np
import re, sys
from aoc_utils import intify, neigh4, neigh8

# tags: 3d grid, falling bricks, topological sort, dfs

ans=0
# list of 3D bricks (start x,y,z ~ end x,y,z)
s='''1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9'''
# data=s
bricks = []
a = data.split('\n')
for l in a:
    b = l.split('~')
    bricks.append([list(int(x) for x in b[0].split(',')), list(int(x) for x in b[1].split(','))])

bricks = np.array(bricks, dtype=int)

grid = np.zeros((10,10,np.max(bricks[:,:,2])+2), dtype=int)
for i in range(len(bricks)):
    grid[bricks[i,0,0]:bricks[i,1,0]+1, bricks[i,0,1]:bricks[i,1,1]+1, bricks[i,0,2]:bricks[i,1,2]+1] = i+1

zorder = np.argsort(bricks[:,0,2])

while True:
    moved = False
    #make the bricks fall until z=1
    for ix in zorder:
        b = bricks[ix]
        z1 = b[0,2]
        zlen = b[1,2]-b[0,2]+1
        while z1>1 and np.all(grid[b[0,0]:b[1,0]+1, b[0,1]:b[1,1]+1, z1-1]==0):
            z1 -= 1
        if z1<b[0,2]:
            # remove the old brick from grid
            grid[b[0,0]:b[1,0]+1, b[0,1]:b[1,1]+1, b[0,2]:b[1,2]+1] = 0
            # add in the position with b[1,2] = z1
            grid[b[0,0]:b[1,0]+1, b[0,1]:b[1,1]+1, z1:z1+zlen] = ix+1
            bricks[ix,:,2]-=b[0,2]-z1
            moved = True
            # print(ix+1, bricks[ix], z1)
            # print(grid.sum(axis=1))
    if not moved: break

from collections import defaultdict

supports = {}
supported = {}

for i,b in enumerate(bricks):
    # check if there is any brick on top of b
    # print(i, b)
    top = grid[b[0,0]:b[1,0]+1, b[0,1]:b[1,1]+1, b[1,2]+1]
    if np.all(top==0):
        pass
        # ans += 1
    else:
        # get all bricks in the top
        top = np.unique(top[top>0])
        supports[i+1] = top
        supported
        for t in top:
            bt = bricks[t-1]
            below_t = grid[bt[0,0]:bt[1,0]+1, bt[0,1]:bt[1,1]+1, bt[0,2]-1]
            # print(f"grid under {t}:", below_t)
            below = np.unique(below_t[below_t>0])
            if t not in supported: supported[t] = below

from functools import cache
from collections import deque

@cache
def dfs(n):
    if n not in supports: return set()
    q = deque(supports[n])
    dropped = {n}
    res = -1
    while q:
        a = q.popleft()
        if all(b in dropped for b in supported[a]):
            dropped.add(a)
            q.extend(supports[a]) if a in supports else None
    return dropped
    
ans = {s: dfs(s) for s in supports}
ans = sum(len(ans[s])-1 for s in ans)

print(ans)
submit(ans)