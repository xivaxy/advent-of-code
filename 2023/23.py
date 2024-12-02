from aocd import data, submit
from aocd.models import Puzzle
import numpy as np
import re, sys
from aoc_utils import intify, neigh4, neigh8
import networkx as nx

# tags: maze, longest path, bfs
# medium. networkx helps iterating over all paths

ans=0
s='''#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#'''
# data=s

# find the longest path from top to bottom

a = data.splitlines()
h,w = len(a), len(a[0])
start = (0, 1)
finish = (h-1, w-2)


# corresponding to neigh4
open_directions = ['v', '<', '^', '>']

def step_in_direction(st: tuple, i: int):
    return (st[0]+neigh4[i][0], st[1]+neigh4[i][1])

def find_neighs(st: tuple):
    assert a[st[0]][st[1]] == '.'
    res = []
    for i in range(4):
        p1 = step_in_direction(st, i)
        if 0<=p1[0]<h and a[p1[0]][p1[1]] in ('.', open_directions[i]):
            cnt = 1
            p0 = st
            node = None
            while True:
                for j in range(4):
                    p2 = step_in_direction(p1, j)
                    if p2!=p0 and a[p2[0]][p2[1]]!="#":
                        cnt+=1
                        if p2==finish:
                            node = p2
                            res.append((node, cnt))
                            break
                        if a[p2[0]][p2[1]]=='.':
                            p0 = p1
                            p1 = p2
                            break
                        if a[p2[0]][p2[1]]==open_directions[j]:
                            cnt += 1
                            node = step_in_direction(p2, j)
                            res.append((node, cnt))
                            break
                if node:
                    break
    return res

q = {start}
scanned = {finish}
G = nx.Graph()
G.add_nodes_from([start, finish])
while q:
    st = q.pop()
    neighs = find_neighs(st)
    scanned.add(st)
    for n, w in neighs:
        G.add_edge(st, n, weight=w)
        if n not in scanned:
            q.add(n)

# go over all paths from start to finish
max_weight = 0
for path in nx.all_simple_paths(G, source=start, target=finish):
    weight = 0
    for i in range(len(path)-1):
        weight += G[path[i]][path[i+1]]['weight']
    max_weight = max(max_weight, weight)

ans = max_weight
print(ans)
submit(ans)