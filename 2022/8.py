from aocd import data, lines, numbers, submit
import numpy as np
from aoc_utils import neigh4

a = np.array([list(map(int, l)) for l in lines], dtype=int)
mark = np.zeros_like(a, dtype=int)
m,n = a.shape
for i in range(m):
    h = -1
    for j in range(n):
        if a[i,j]>h:
            mark[i,j]=1
            h=a[i,j]
    h = -1
    for j in reversed(range(n)):
        if a[i,j]>h:
            mark[i,j]=1
            h=a[i,j]
    
for j in range(n):
    h = -1
    for i in range(m):
        if a[i,j]>h:
            mark[i,j]=1
            h=a[i,j]
    h = -1
    for i in reversed(range(m)):
        if a[i,j]>h:
            mark[i,j]=1
            h=a[i,j]

submit(mark.sum())

views = np.zeros((4, m, n), dtype=int)
for ii,di in enumerate(neigh4):
    print(di)
    for i in range(m):
        for j in range(n):
            x,y = i,j
            x+=di[0]
            y+=di[1]
            while 0<=x<m and 0<=y<n:
                views[ii,i,j]+=1
                if a[i,j]>a[x,y]:
                    x+=di[0]
                    y+=di[1]
                else:
                    break
submit(views.prod(axis=0).max())