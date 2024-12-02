from aocd import data, lines, numbers, submit
import numpy as np
import re
import sys
from aoc_utils import intify, neigh4, neigh8
import networkx as nx

dat = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II"""

a = intify([re.match(r"Valve (..) has flow rate=(\d+); tunnel.? lead.? to valve.? (.+)", l).groups() for l in data.splitlines()])
g = {}
f = {}
F = []
for t in a:
    t[2] = t[2].split(", ")
    g[t[0]] = t[2]
    f[t[0]] = t[1]
    if t[1]>0:
        F.append((t[1], t[0]))

G = nx.DiGraph(g)
shortest = dict(nx.all_pairs_shortest_path_length(G))
F.sort(reverse=True)
Find = {}
for i, (flow, node) in enumerate(F):
    Find[node] = 1<<i

cache = {}

# def dfs(st, dur, opened):
#     if (st, dur, opened) in cache:
#         return cache[(st, dur, opened)]
#     res = 0
#     if dur>1:
#         if st in Find and (Find[st]&opened==0):
#             res = dfs(st, dur-1, Find[st]|opened) + (dur-1)*f[st]
#         for n in g[st]:
#             res = max(res, dfs(n, dur-1, opened))
#     cache[(st, dur, opened)] = res
#     return res

# def dfs(st, el, dur, opened, srcst=None, srcel=None):
#     if (st, el, dur, opened) in cache:
#         return cache[(st, el, dur, opened)]
#     res = 0
#     if dur>1:
#         if st in Find and (Find[st]&opened==0):
#             res = max(res, (dur-1)*f[st])
#             for m in g[el]:
#                 if m==srcel:
#                     continue
#                 res = max(res, dfs(st, m, dur-1, Find[st]|opened, st, el) + (dur-1)*f[st])
#             if el!=st and el in Find and (Find[el]&opened==0):
#                 res = max(res, dfs(st, el, dur-1, Find[st]|Find[el]|opened, st, el) + (dur-1)*(f[st]+f[el]))
#         if el!=st and el in Find and (Find[el]&opened==0):
#             res = max(res, (dur-1)*f[el])
#             for n in g[st]:
#                 if n==srcst:
#                     continue
#                 res = max(res, dfs(n, el, dur-1, Find[el]|opened, st, el) + (dur-1)*f[el])
#         for n in g[st]:
#             for m in g[el]:
#                 if st==el and m<n:
#                     continue
#                 if n==srcst or m==srcel:
#                     continue
#                 res = max(res, dfs(n, m, dur-1, opened, st, el))
#                 if dur>=25:
#                     print(res, st, el, dur, opened)
#     cache[(st, el, dur, opened)] = res
#     return res

# submit(dfs('AA', 'AA', 26, 0))



# from matplotlib import pyplot as plt
# nx.draw_networkx(G, node_size=[f[n]*10 if f[n] else 100 for n in G ], node_color=['red' if f[n] else 'green' for n in G ])
# plt.show()

no1 = [
    "YP",
    "NM",
    "YH",
    "XK",
    "XS",
    "EI",
    "MW",
    "RA",
]
no2 = [
    "QC",
    "WK",
    "NU",
    "CX",
    "NC",
    "ZG",
    "EA",
]

def dfs(st, dur, nodes, visited):
    if len(visited)==len(nodes):
        return 0
    if dur<=1:
        return 0
    res = 0
    for n in nodes:
        if n not in visited:
            visited.add(n)
            res = max(res, dfs(n, dur-shortest[st][n]-1, nodes, visited) + (dur-shortest[st][n]-1)*f[n])
            visited.remove(n)
    return res

a1 = dfs('AA', 26, no1, set())
a2 = dfs('AA', 26, no2, set())
print(a1, a2, a1+a2)
submit(a1+a2)

# print(sorted([(shortest[n][m], n,m) for n in Find.keys() for m in Find.keys() if m>=n]))