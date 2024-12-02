import sys
from aocd import data, lines, numbers, submit
import numpy as np
from aoc_utils import intify

dat = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""
dat.splitlines()

paths = [intify([p.split(",") for p in l.split(" -> ")]) for l in lines]
ar = np.array(paths[0], dtype=int)
for p in paths[1:]:
    ar = np.vstack((ar, p))

print(ar.shape)
Ms= ar.max(axis=0)
ms = ar.min(axis=0)
print(ms, Ms)

a = np.zeros((500+Ms[1]+4, Ms[1]+4), dtype=int)
for path in paths:
    x,y = path[0]
    for x2,y2 in path[1:]:
        if x==x2:
            a[x,min(y, y2):max(y,y2)+1]=1
        elif y==y2:
            a[min(x, x2):max(x,x2)+1, y]=1
        else:
            raise
        x,y = x2, y2

a[500-Ms[1]-3:500+Ms[1]+4, Ms[1]+2]=1

def printa(a):
    for i in range(a.shape[1]):
        print("".join(a[:,i].astype(str)))

ans = 0
while True:
    drop = np.array([500, 0], dtype=int)
    if a[tuple(drop)]==2:
        print(ans)
        submit(ans)
        # printa(a[485:515, :])
        sys.exit()
    while True:
        if a[tuple((f:=drop+[0,1]))]==0:
            drop=f
        elif a[tuple((f:=drop+[-1,1]))]==0:
            drop=f
        elif a[tuple((f:=drop+[1,1]))]==0:
            drop=f
        else:
            a[tuple(drop)]=2
        # if drop[1]>Ms[1] or not ms[0]<=drop[0]<=Ms[0]:
        #     submit(ans)
        #     sys.exit()
        if a[tuple(drop)]==2:
            ans+=1
            break