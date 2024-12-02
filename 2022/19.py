# from aocd import data, lines, numbers, submit
import numpy as np
import re
import sys
# from aoc_utils import intify, neigh4, neigh8

def intify(a: list, output_tuples = False):
    are_input_tuples = not isinstance(a[0], list)
    for i in range(len(a)):
        if are_input_tuples:
            b = list(a[i])
        else:
            b = a[i]
        for j in range(len(b)):
            try:
                b[j] = int(b[j])
            except:
                pass
        if output_tuples:
            a[i] = tuple(b)
        elif are_input_tuples:
            a[i] = b
    return a

# Blueprint 25: Each ore robot costs 4 ore. Each clay robot costs 3 ore. Each obsidian robot costs 2 ore and 19 clay. Each geode robot costs 3 ore and 10 obsidian.
dat = """Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian."""

data = """Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 2 ore and 11 clay. Each geode robot costs 4 ore and 8 obsidian.
Blueprint 2: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 2 ore and 16 clay. Each geode robot costs 4 ore and 16 obsidian.
Blueprint 3: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 18 clay. Each geode robot costs 2 ore and 11 obsidian."""

bps = intify([re.match(r"Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.", l).groups() for l in data.splitlines()])

T=32
ans = 1

id, orec, clayc, obc1, obc2, gec1, gec2 = 0,0,0,0,0,0,0
cost = np.zeros((4,4), dtype=int)
cost[0,0], cost[1,0], cost[2, 0], cost[2,1], cost[3,0], cost[3,2] = orec, clayc, obc1, obc2, gec1, gec2
mins = np.array([0,0,0,0], dtype=int)
robs = np.array([1,0,0,0], dtype=int)
robnew = np.eye(4, dtype=int)
ore, clay, ob, ge = 0,0,0,0
orer, clayr, obr, ger = 1,0,0,0
cache = {}

def dfs(t, mins, robs, wait = -1):
    if t==T:
        return mins[3]
    if t==T-1:
        return mins[3]+robs[3]
    if t==T-2:
        ret = mins[3]+robs[3]*2
        if np.all(mins>=cost[3]):
            ret = max(ret, mins[3]+robs[3]*2+1)
        return ret
    key = (t, tuple(mins), tuple(robs), wait)
    if key in cache:
        return cache[key]
    ret = 0
    if wait>=0:
        if np.all(mins>=cost[wait,:]):
            ret = dfs(t+1, mins+robs-cost[wait,:], robs+robnew[wait])
        else:
            ret = dfs(t+1, mins+robs, robs, wait)
    else:
        for w in range(3,-1,-1):
            if t>15 and w==0:
                continue
            if t>22 and w==1:
                continue
            if np.all(cost[w]<=robs*25):
                ret = max(ret, dfs(t, mins, robs, w))
    
    cache[key] = ret
    return ret
    
for l in bps:
    id, cost[0,0], cost[1,0], cost[2, 0], cost[2,1], cost[3,0], cost[3,2] = l
    cache = {}
    ge = dfs(0, mins, robs)
    ans*=ge
    print(id, ge)

print(ans)
# 31, 9, 19 = 5301 , t 17, 21
