from aocd import data, submit
from aocd.models import Puzzle
import numpy as np
import re, sys
from aoc_utils import intify, neigh4, neigh8

ans=0
s='''LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)'''
# data=s

route = [0 if c=="L" else 1 for c in data.split('\n\n')[0]]
places = {}
for line in data.split('\n\n')[1].split('\n'):
    line = line.split(' = ')
    places[line[0]] = line[1].replace('(', '').replace(')', '').split(', ')

cur = [k for k in places.keys() if k[-1] == 'A']
n = len(cur)
print(len(route))
print(cur)

routes = {}
routes_names = {}
for c0 in cur:
    routes[c0] = []
    routes_names[c0] = []
    c = c0
    ptr = 0
    visited = set()
    while True:
        routes_names[c0].append((c, ptr))
        routes[c0].append(1 if c[-1] == 'Z' else 0)
        visited.add((c, ptr))
        
        c = places[c][route[ptr]]
        ptr  = (ptr+1)%len(route)
        if (c, ptr) in visited:
            loop_start = routes_names[c0].index((c, ptr))
            print(c0, np.nonzero(routes[c0])[0])
            routes[c0] = (len(routes[c0]), len(routes[c0])-loop_start, np.nonzero(routes[c0])[0][0], loop_start)
            break

print(routes)
modrems = [ (m, r%m) for _, m, r, _ in routes.values() ]
print(modrems)
import math
ans = math.lcm(*[m for m, _ in modrems])

print(ans)
# submit(ans)