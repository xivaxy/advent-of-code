# Lobby Layout (Hexagonal tiles game of life)
from common import INPUT_DIR
import os
import re

DAY = os.path.basename(__file__)[:-3]
input_path = f"{INPUT_DIR}\\{DAY}.txt"

with open(input_path) as f:
    data = f.read().strip().splitlines()
    n = len(data)
    print(f"Read {n} lines from {input_path}")


data = [[t[0] for t in re.findall(r"((n|s)?[ew])", d)] for d in data]

grid = {}
dirs = {
    "e": (1, 0),
    "w": (-1, 0),
    "ne": (1, 1),
    "se": (0, -1),
    "nw": (0, 1),
    "sw": (-1, -1),
}

for d in data:
    c = [0, 0]
    for t in d:
        c[0] += dirs[t][0]
        c[1] += dirs[t][1]
    t = tuple(c)
    if t not in grid:
        grid[t] = 1
    else:
        grid[t] = 1 - grid[t]

print("Part1", sum(grid.values()))

for st in range(100):
    nearblack = set()
    for k, v in grid.items():
        if v == 1:
            nearblack.add(k)
            for y in dirs.values():
                nearblack.add((k[0] + y[0], k[1] + y[1]))

    grid_new = {}
    for x in nearblack:
        num = sum(grid.get((x[0] + y[0], x[1] + y[1]), 0) for y in dirs.values())
        if x not in grid or grid[x] == 0:
            if num == 2:
                grid_new[x] = 1
        elif grid[x] == 1:
            if num == 1 or num == 2:
                grid_new[x] = 1

    grid = grid_new


print("Part2", sum(grid.values()))
