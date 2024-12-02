from aocd import data, lines, numbers, submit
import numpy as np
import re
import sys
from aoc_utils import intify, neigh4, neigh8, neigh6

cubes = np.array([list(eval(l)) for l in lines], dtype=int)
a = np.zeros(cubes.max(axis=0)+2, dtype=int)
for c in cubes:
    a[tuple(c)] = 1

ans = 0

def dfs(b):
    a[tuple(b)]=-1
    for ddx,ddy,ddz in neigh6:
        bn = b + [ddx,ddy,ddz]
        if np.all(bn>=0) and np.all(bn<a.shape) and a[tuple(bn)]==0:
            dfs(bn)

q = [np.zeros((3,), dtype=int)]
i=0
while i<len(q):
    b = q[i]
    for ddx,ddy,ddz in neigh6:
        bn = b + [ddx,ddy,ddz]
        if np.all(bn>=0) and np.all(bn<a.shape) and a[tuple(bn)]==0:
            a[tuple(bn)]=-1
            q.append(bn)
    i+=1


for ii,c in enumerate(cubes):
    for dx,dy,dz in neigh6:
        t = c + [dx,dy,dz]
        if a[tuple(t)]==-1:
            ans+=1

print(ans)
submit(ans) 
