# Toboggan Trajectory
from common import INPUT_DIR
import math

data = []

with open(f"{INPUT_DIR}\\3.txt") as f:
    for line in f:
        line = line.strip()
        data.append(line)

n = len(data)
print(len(data))
m = len(data[0])
s = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
res = []
for a, b in s:
    result = 0
    i = 0
    x = 0
    while i + b < n:
        i += b
        x = (x + a) % m
        if data[i][x] == "#":
            result += 1
    res.append(result)


print(res)
print(math.prod(res))
