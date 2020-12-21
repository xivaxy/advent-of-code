# Seating System ("Game of Life")
from common import INPUT_DIR
import os
from copy import deepcopy

DAY = os.path.basename(__file__)[:-3]
input_path = f"{INPUT_DIR}\\{DAY}.txt"

with open(input_path) as f:
    data = f.read().strip().splitlines()
    n = len(data)
    print(f"Read {n} lines from {input_path}")


m = len(data[0])

data = [list(d) for d in data]


def occupied_near(a, b):
    cnt = 0
    for i in (a - 1, a, a + 1):
        for j in (b - 1, b, b + 1):
            if 0 <= i < n and 0 <= j < m and (i, j) != (a, b):
                if data[i][j] == "#":
                    cnt += 1
    return cnt


def occupied_directions(a, b):
    cnt = 0
    for i in (-1, 0, +1):
        for j in (-1, 0, +1):
            if (i, j) != (0, 0):
                c = 1
                while (
                    0 <= a + c * i < n
                    and 0 <= b + c * j < m
                    and data[a + c * i][b + c * j] == "."
                ):
                    c += 1
                if (
                    0 <= a + c * i < n
                    and 0 <= b + c * j < m
                    and data[a + c * i][b + c * j] == "#"
                ):
                    cnt += 1
    return cnt


data2 = deepcopy(data)

while True:
    state_changed = False
    for i in range(n):
        for j in range(m):
            if data[i][j] == "L" and occupied_directions(i, j) == 0:
                data2[i][j] = "#"
                state_changed = True
            elif data[i][j] == "#" and occupied_directions(i, j) >= 5:
                data2[i][j] = "L"
                state_changed = True
            else:
                data2[i][j] = data[i][j]
    data = data2
    data2 = deepcopy(data)
    if not state_changed:
        print(sum(1 for i in range(n) for j in range(m) if data[i][j] == "#"))
        break
