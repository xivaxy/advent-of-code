# Rain Risk (Ferry maneuvres)
from common import INPUT_DIR
import os
from copy import deepcopy
import math

DAY = os.path.basename(__file__)[:-3]
input_path = f"{INPUT_DIR}\\{DAY}.txt"

with open(input_path) as f:
    data = f.read().strip().splitlines()
    n = len(data)
    print(f"Read {n} lines from {input_path}")

# m = len(data[0])

pos = [0, 0]
di = 0

for d in data:
    w = d[0]
    r = int(d[1:])
    if w == "N":
        pos[1] += r
    elif w == "S":
        pos[1] -= r
    elif w == "E":
        pos[0] += r
    elif w == "W":
        pos[0] -= r
    elif w == "L":
        di = (di + r) % (360)
    elif w == "R":
        di = (di - r + 360) % 360
    elif w == "F":
        pos[0] += r*math.cos(di/180*math.pi)
        pos[1] += r*math.sin(di/180*math.pi)

print(abs(pos[0]) + abs(pos[1]))

ship = [0, 0]
pos = [10, 1]
# di = 0

# data = ["F10",
#         "N3",
#         "F7",
#         "R90",
#         "F11"]

for d in data:
    w = d[0]
    r = int(d[1:])
    dx = pos[0]-ship[0]
    dy = pos[1] - ship[1]
    if w == "N":
        pos[1] += r
    elif w == "S":
        pos[1] -= r
    elif w == "E":
        pos[0] += r
    elif w == "W":
        pos[0] -= r
    elif w == "L":
        while r > 0:
            pos = [-pos[1], pos[0]]
            r -= 90
    elif w == "R":
        while r > 0:
            pos = [pos[1], -pos[0]]
            r -= 90
    elif w == "F":
        ship[0] += pos[0]*r
        ship[1] += pos[1]*r
    # print(ship, pos)

print(abs(ship[0]) + abs(ship[1]))
# print(abs(ship[0]) + abs(ship[1]))
