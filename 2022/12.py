import sys
from aocd import data, lines, numbers, submit
import numpy as np

from aoc_utils import neigh4

grid = [list(l) for l in lines]
m = len(grid)
n = len(grid[0])

for i in range(m):
    for j in range(n):
        if grid[i][j]=='S':
            start = (i,j)
            grid[i][j] = 'a'
        if grid[i][j]=='E':
            goal = (i,j)
            grid[i][j] = 'z'
grid = [[ord(c)-ord('a') for c in l] for l in grid]
grid = np.array(grid, dtype=int)
print(start, goal)
acells = set((i,j) for i in range(m) for j in range(n) if grid[i,j]==0)

q = [goal]
q2 = []
vis = set([goal])
step = 1
while q:
    q2 = []
    for cn in q:
        x,y = cn
        for dx,dy in neigh4:
            x=cn[0]+dx
            y=cn[1]+dy
            if 0<=x<m and 0<=y<n and (x,y) not in vis and grid[cn]-grid[x,y]<=1:
                if (x,y) in acells:
                    submit(step)
                    sys.exit()
                vis.add((x,y))
                q2.append((x,y))
    q=q2
    step+=1


