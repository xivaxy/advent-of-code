# Ticket Translation (bipartite graph matching)
from common import INPUT_DIR
from networkx.algorithms import bipartite
import os
import math
from collections import defaultdict
from random import shuffle
import networkx as nx
import logging
from z3 import *

DAY = os.path.basename(__file__)[:-3]
input_path = f"{INPUT_DIR}\\{DAY}.txt"

with open(input_path) as f:
    data = f.read().strip()
    n = len(data)
    print(f"Read {n} lines from {input_path}")

data = data.split("\n\n")
assert(len(data) == 3)
rules = data[0].split("\n")
rules = {r.split(":")[0]: [tuple(int(a) for a in cond.strip().split("-"))
                           for cond in r.split(":")[1].split("or")]
         for r in rules}

your = data[1]
near = [list(map(int, t.strip().split(","))) for t in data[2].split("\n")[1:]]
print(f"orig near len {len(near)}")


def valid(x):
    return any(map(lambda y: y[0][0] <= x <= y[0][1]
                   or y[1][0] <= x <= y[1][1], rules.values()))


# part 1
res = 0

for ne in near:
    res += sum(num for num in ne if not valid(num))

print(f"Part1: {res}")


near = [ne for ne in near if all(map(valid, ne))]
near.append(list(map(int, your.split("\n")[1].split(","))))
N = len(rules)
fields = [[ne[i] for ne in near] for i in range(N)]
rul = [(k, v) for k, v in rules.items()]
ass = []


def dep():
    return math.prod(near[-1][i] for i, f in enumerate(ass) if rul[f][0].startswith("departure"))


field_name = {}


def valid_field(field, rule):
    if (field, rule) in field_name:
        return field_name[(field, rule)]
    rr = rul[rule][1]
    res = all(map(lambda f: rr[0][0] <= f <= rr[0][1]
                  or rr[1][0] <= f <= rr[1][1], fields[field]))
    field_name[(field, rule)] = res
    return res

for i in range(N):
    for j in range(N):
        rr = rul[j][1]
        field_name[(i, j)] = all(map(lambda f: rr[0][0] <= f <= rr[0][1]
                                     or rr[1][0] <= f <= rr[1][1], fields[i]))
# networkX bipartite matching algo
g = nx.Graph()
g.add_nodes_from(range(N), bipartite=0)
g.add_nodes_from(range(N, 2*N), bipartite=1)
g.add_edges_from((i, j+N) for i in range(N)
                 for j in range(N) if field_name[(i, j)])
matching = bipartite.maximum_matching(g)
ass = [x for _, x in sorted((i, j-N)
                            for i, j in matching.items() if i < N)]
print(f"Part2: {dep()}")

# Sorting + backtracking
counts = [(i, sum(1 for j in range(N) if field_name[(i, j)]), sum(
    1 for j in range(N) if field_name[(j, i)])) for i in range(N)]
fields_sorted = list(map(lambda x: x[0], sorted(counts, key=lambda x: x[1])))
names_sorted = list(map(lambda x: x[0], sorted(counts, key=lambda x: x[2])))

ass = []  # index into fields_sorted
asss = set()
NUMS = [10, 4, 5, 8, 18, 17, 0, 7, 13, 15, 16, 14, 3, 12, 2, 6, 1, 19, 9, 11]
print("Computing by backtracking")
done = False


def dfs():
    global done
    global ass
    if done:
        return
    if len(ass) == N:
        ass = [a for _, a in sorted(zip(fields_sorted, ass))]
        print(f"{ass=}")
        print(f"Part2: {dep()}")
        done = True
        return
    for i in range(N):
        if i not in asss and field_name[(fields_sorted[len(ass)], i)]:
            ass.append(i)
            asss.add(i)
            dfs()
            ass.pop()
            asss.remove(i)

dfs()

# z3 SAT solver
print("Computing by z3 SAT solver")
s = Solver()
vr = [Int(str(i)) for i in range(N)]
s.add(([Or([vr[i] == j for j in range(N) if field_name[i,j]]) for i in range(N)]))
s.add(Distinct(vr))
s.check()
ass = [s.model().eval(vr[i]).as_long() for i in range(N)]
print("Part2:", dep())
