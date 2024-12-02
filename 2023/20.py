from aocd import data, submit
from aocd.models import Puzzle
import numpy as np
import re, sys
from aoc_utils import intify, neigh4, neigh8, first_intersection

# tags: parsing, logical gates with states, first intersection of rare events

ans=0
s=r'''broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output'''
# data=s
modules = {}
for l in data.splitlines():
    name, dest = l.split(" -> ")
    if name[0] in "%&":
        modules[name[1:]] = (name[0], dest.split(", "))
    else:
        modules[name] = ("", dest.split(", "))

states = {k: 0 if v[0]=="%" else [] for k,v in modules.items() if v[0]!="" }

nand_inp = {k: [] for k,v in modules.items() if v[0]=="&" } # for not-and modules
for k,v in modules.items():
    for dest in v[1]:
        if dest in nand_inp: # dest is not-and module
            nand_inp[dest].append(k)
            if isinstance(states[dest], int):
                states[dest] = []
            states[dest].append(0)

from collections import deque
q = deque()  # queue for signals passed between modules
counts = [0,0]

final = "mf"
lows = [[] for _ in range(len(nand_inp[final]))]

for i in range(100000):
    q.append((0, "input", "broadcaster"))  # (signal, sender, reciever)
    while q:
        signal, sender, rec = q.popleft()
        counts[signal]+=1
        if rec=="rx":
            continue
        if rec in nand_inp[final] and signal==0:
            lows[nand_inp[final].index(rec)].append(i)
            if all(len(lw)>2 for lw in lows):
                ans = first_intersection(lows)
                print(ans)
                submit(ans)
                sys.exit()
        t, dests = modules[rec]
        match t:
            case "%":
                if signal==0:
                    states[rec] = 1-states[rec]
                    for dest in dests:
                        q.append((states[rec], rec, dest))
            case "&":
                states[rec][nand_inp[rec].index(sender)] = signal
                if all(states[rec]):
                    for dest in dests:
                        q.append((0, rec, dest))
                else:
                    for dest in dests:
                        q.append((1, rec, dest))
            case "":
                for dest in dests:
                    q.append((0, rec, dest))

# ans = counts[0]*counts[1]
# print(ans)
# submit(ans)