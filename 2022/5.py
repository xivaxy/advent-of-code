import re
from aocd import data, lines, numbers, submit
import numpy as np

from aoc_utils import intify

stk, inst = data.split("\n\n")
stk = stk.split("\n")[::-1]
l = (len(stk[0])+1)//4
stacks = [[] for _ in range(l)]
for le in stk[1:]:
    for i in range(l):
        c = le[i*4+1]
        if 'A'<=c<='Z':
            stacks[i].append(c)
inst = intify([re.match(r"move (\d+) from (\d+) to (\d+)", li).groups() for li in inst.split("\n")])
for cnt, fr, to in inst:
    stacks[to-1].extend(stacks[fr-1][-cnt:])
    for i in range(cnt):
        stacks[fr-1].pop()

submit("".join(st[-1] for st in stacks))