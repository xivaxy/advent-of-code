from aocd import data, lines, numbers, submit
import numpy as np
import re
import sys
from aoc_utils import intify, neigh4, neigh8

dat = """        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5"""


ma = data.split("\n\n")[0].splitlines()
inst = data.split("\n\n")[1]
n = len(ma[10])
m = len(ma)
print(m,n)
y = None
a = np.zeros((m,n), dtype=int)
rowedges = []
for i in range(m):
    for j in range(len(ma[i])):
        match ma[i][j]:
            case '.': 
                a[i,j] = 1
                if y is None and i==0:
                    y = j
            case '#': a[i,j] = 2


i = 0
ins = []
tm ={'R':1, 'L':-1}
for j in range(1, len(inst)):
    if inst[j] in "RL":
        if ins:
            ins.append((tm[inst[i]], int(inst[i+1:j])))
        else:
            ins.append((None, int(inst[:j])))
        i = j
ins.append((tm[inst[i]], int(inst[i+1:])))
# print(ins)
# 10R5L5R10L4R5L5

rowedges = []
for i in range(m):
    st = e = None
    for j in range(n):
        if a[i][j]>0:
            if st is None:
                st = j
            e = j
    rowedges.append((st,e))

coledges = []
for j in range(n):
    st = e = None
    for i in range(m):
        if a[i][j]>0:
            if st is None:
                st = i
            e = i
    coledges.append((st,e))

x = 0
di = 0
dis = [(0,1), (1, 0), (0,-1), (-1, 0)]
# xy=
assert y == rowedges[0][0]

def mod(x, edges:tuple):
    st,e = edges
    return (x-st)%(e-st+1)+st

def mod6(x,y,di):
    if di in [0,2] and rowedges[x][0]<=y<=rowedges[x][1]:
            return x,y,di
    elif di in [1,3] and coledges[y][0]<=x<=coledges[y][1]:
            return x,y,di
 ##
 #
##
#
    match di:
        case 0:
            match x//50:
                case 0: assert y==150; X,Y,D = 149-x, 99, 2   # 1
                case 1: assert y==100; X,Y,D = 49, 50+x, 3    # 2
                case 2: assert y==100; X,Y,D = 149-x, 149, 2  # 1
                case 3: assert y==50; X,Y,D = 149, x-100, 3   # 3
        case 2:
            match x//50:
                case 0: assert y==49; X,Y,D = 149-x, 0, 0   # 4
                case 1: assert y==49; X,Y,D = 100, x-50, 1  # 5
                case 2: assert y==-1; X,Y,D = 149-x, 50, 0  # 4
                case 3: assert y==-1; X,Y,D = 0, x-100, 1   # 6
        case 1:
            match y//50:
                case 0: assert x==200; X,Y,D = 0, y+100, 1   # 7
                case 1: assert x==150; X,Y,D = y+100, 49, 2  # 3
                case 2: assert x==50; X,Y,D = y-50, 99, 2    # 2
        case 3:
            match y//50:
                case 0: assert x==99; X,Y,D = y+50, 50, 0    # 5
                case 1: assert x==-1; X,Y,D = y+100, 0, 0    # 6
                case 2: assert x==-1; X,Y,D = 199, y-100, 3  # 7
    return X,Y,D


for turn, d in ins:
    if turn is not None:
        di = (di+turn)%4
    for i in range(d):
        x2=x+dis[di][0]
        y2=y+dis[di][1]
        # if di in [0,2]:
        #     y2 = mod(y2, rowedges[x])
        # else:
        #     x2 = mod(x2, coledges[y])
        X,Y,D = mod6(x2, y2, di)
        if a[X,Y]==2:
            break
        assert a[X,Y]==1, f"{x=}, {y=}, {di=}, {X=}, {Y=}, {D=}, "
        x,y,di = X,Y,D

ans = 1000*(x+1)+4*(y+1)+di
print(x,y,di, ans)
submit(ans)

