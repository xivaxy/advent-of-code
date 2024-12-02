from aocd import data, submit
from aocd.models import Puzzle
import numpy as np
import re, sys
from aoc_utils import intify, neigh4, neigh8

# tags: graph, minimal cost path, dijkstra, networkx

ans=0
s='''2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533'''
# data=s
a = data.splitlines()
b = [list(l) for l in a]
a = intify(b)  # costs for each cell
h,w = len(a), len(a[0])
start = (0,0)
finish = (h-1,w-1)
# find a path to minimize cost from start to finish
# can move at most three blocks in a single direction before it must turn 90 degrees left or right
# can't move diagonally
import networkx as nx
G = nx.DiGraph()
for x in range(h):
    for y in range(w):
        if x==0 and y==0:
            continue
        for d1 in range(4):
            # (x,y, d1) next node - continue moving in same direction
            for st in range(1,10):
                nxt = (x+neigh4[d1][0], y+neigh4[d1][1], d1, st+1)
                if 0<=nxt[0]<h and 0<=nxt[1]<w:
                    # if finish node, add without d and st
                    if nxt[0]==h-1 and nxt[1]==w-1 and st+1>=4:
                        G.add_edge((x,y, d1, st), finish, weight=a[nxt[0]][nxt[1]])
                    else:
                        G.add_edge((x,y, d1, st), nxt, weight=a[nxt[0]][nxt[1]])
            for d2 in range(4):
                # (x,y, d2) next node - was moving in a different direction
                if d1==d2 or abs(d1-d2)==2: # same direction or opposite direction
                    continue
                nxt = (x+neigh4[d2][0], y+neigh4[d2][1], d2, 1)
                if 0<=nxt[0]<h and 0<=nxt[1]<w:
                    for st in range(4,11):
                        # if nxt[0]==h-1 and nxt[1]==w-1:
                        #     G.add_edge((x,y, d1, st), finish, weight=a[nxt[0]][nxt[1]])
                        # else:
                        G.add_edge((x,y, d1, st), nxt, weight=a[nxt[0]][nxt[1]])
G.add_edge(start, (1,0,0,1), weight=a[1][0])
G.add_edge(start, (0,1,3,1), weight=a[0][1])
# find shortest path from start to any finish node
ans, path = nx.single_source_dijkstra(G, start, finish)
dir_characters = ['v', '<', '^', '>']
# for (x,y,d,st) in path[1:-1]:
#     print(x,y,d,st)
#     b[x][y] = dir_characters[d]
# print('\n'.join(''.join(l) for l in b))

print(ans)
submit(ans)