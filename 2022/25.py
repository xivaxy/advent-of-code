from aocd import data, lines, numbers, submit
import numpy as np
import re
import sys
import math
from aoc_utils import intify, neigh4, neigh8

dm = {"-":-1, "=":-2}
md = {-1:"-", -2:"="}
su = 0
for l in lines:
    ac = 0
    for c in l:
        ac*=5
        ac+=int(c) if c in "012" else dm[c]
    su+=ac

print(su)
ans = ""
while su>0:
    su, re = su//5, su%5
    if re>=3:
        re-=5
        re = md[re]
        su+=1
    ans = str(re) + ans
submit(ans)