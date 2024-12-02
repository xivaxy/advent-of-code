from aocd import data, lines, numbers, submit
import numpy as np
import re
import sys
from aoc_utils import intify, neigh4, neigh8

ma = data.splitlines()
n = len(ma[10])
m = len(ma)
# print(m,n)
ma = [[0 if c=='.' else 1 for c in l] for l in ma]

elfs = []
for i in range(m):
    for j in range(n):
        if ma[i][j]==1:
            elfs.append((i,j))

elfsm = set(elfs)
E = len(elfs)
dis = [(-1,0), (1, 0), (0, -1), (0, 1)]
dioff = 0
# eldi = [[0,1,2,3] for i in range(E)]
for r in range(10000):
    print(r)
    prop = {}
    for e in range(E):
        x,y = elfs[e]
        if all((x+dx, y+dy) not in elfsm for dx,dy in neigh8):
            continue
        for d in range(4):
            di = dis[(d+dioff)%4]
            X,Y = (x+di[0], y+di[1])
            if (X,Y) not in elfsm:
                if (di[0]==0 and (x+1, y+di[1]) not in elfsm and (x-1, y+di[1]) not in elfsm) or (di[1]==0 and (x+di[0], y+1) not in elfsm and (x+di[0], y-1) not in elfsm):
                    break
        else:
            continue
        if (X,Y) in prop:
            prop[(X,Y)].append(e)
        else:
            prop[(X,Y)] = [e]
    dioff+=1
    if len(prop)==0:
        submit(r+1)
        sys.exit()
    for (X,Y), l in prop.items():
        if len(l)==1:
            e = l[0]
            x,y = elfs[e]
            elfsm.remove((x,y))
            elfsm.add((X,Y))
            elfs[e] = (X,Y)

x = X = y = Y = 20
for (a,b) in elfs:
    x = min(x, a)
    X = max(X, a)
    y = min(y, b)
    Y = max(Y, b)

ans = (X-x+1)*(Y-y+1)-E
# submit(ans)

