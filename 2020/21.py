# Allergen Assessment (small bipartite matching)
from common import INPUT_DIR
import os
from collections import defaultdict
from z3 import *
from functools import reduce

DAY = os.path.basename(__file__)[:-3]
input_path = f"{INPUT_DIR}\\{DAY}.txt"

with open(input_path) as f:
    data = f.read().strip().splitlines()
    n = len(data)
    print(f"Read {n} lines from {input_path}")

foods = [d.split(" (contains ")[0].split(" ") for d in data]
alr = [d.split(" (contains ")[1].strip(")").split(", ") for d in data]
alrset = reduce(lambda x, y: x.union(y), alr, set())
ingset = reduce(lambda x, y: x.union(y), foods, set())

al2ing = defaultdict(ingset.copy)
for i in range(n):
    for a in alr[i]:
        al2ing[a] = al2ing[a].intersection(foods[i])
al2ing = dict(al2ing)

clean_ings = reduce(lambda x, y: x.difference(y), al2ing.values(), ingset)
res = 0
for i in range(n):
    res += len([1 for ing in foods[i] if ing in clean_ings])

print("Part1:", res)


dirty_ing = ingset.difference(clean_ings)
sol = Solver()
Va = {a: Int(a) for a in alrset}
Vi = {i: Int(i) for i in dirty_ing}
sol.add([Or([Va[a] == Vi[i] for i in ings]) for a, ings in al2ing.items()])
sol.add(Distinct([Va[a] for a in alrset]))
sol.check()
m = sol.model()
A = {m.eval(va).as_long(): a for a, va in Va.items()}
I = {m.eval(vi).as_long(): i for i, vi in Vi.items()}
res = sorted([(al, I[i]) for i, al in A.items()])

print("Part2:", ",".join(s[1] for s in res))
