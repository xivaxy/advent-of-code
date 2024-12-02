from aocd import data, lines, numbers, submit
import numpy as np
import re
import sys
import math
from aoc_utils import intify, neigh4, neigh8

dat = """#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#"""

dis = [(0,1), (1, 0), (0,-1), (-1, 0)]
dis0 = dis + [(0,0)]
a = []
ff = ">v<^."
for l in data.splitlines():
    if l[2]=='#':
        continue
    a.append([ff.index(c) for c in l[1:-1]])

a = np.array(a, dtype=int)
m = len(a)
n = len(a[0])
print(m,n)
mn=math.lcm(m,n)
print(mn)
ma = np.zeros((mn, m, n), dtype=int)
st = np.ones_like(ma)*1000000000
for t in range(mn):
    for i in range(m):
        for j in range(n):
            if a[i,j]<4:
                dx, dy = dis[a[i,j]]
                ma[t, (i+dx*(t+1))%m, (j+dy*(t+1))%n] = 1
print("maps complete")
leg1 = 240
leg2 = 237
stx, sty = 0, 0
ex, ey = -1 , -1
t0 = leg1+leg2

for tau in range(0, mn*10):
    t=tau%mn
    for i in range(m):
        for j in range(n):
            if ma[t,i,j]==0:
                prev = (st[t-1,i+dx,j+dy] for dx, dy in dis0 if 0<=i+dx<m and 0<=j+dy<n and ma[t-1,i+dx,j+dy]==0)
                st[t,i,j] = min(prev, default=1000000000) + 1
    if ma[t,stx,sty]==0:
        st[t,stx,sty]=(t-t0)%mn+1
    if st[t, ex, ey]<1000000000:
        leg3 = st[t, ex, ey]+1
        print(leg3)
        break

ans=leg1+leg2+leg3
print(ans)
submit(ans)