# Adapter Array (dynamic programming)
from common import INPUT_DIR
import os
from collections import defaultdict

DAY = os.path.basename(__file__)[:-3]
input_path = f"{INPUT_DIR}\\{DAY}.txt"

with open(input_path) as f:
    data = f.read().strip().splitlines()
    n = len(data)
    print(f"Read {n} lines from {input_path}")

# m=len(data[0])
res = 0
nw = True
content = {}
containers = defaultdict(list)

data = sorted([int(d) for d in data])
V = max(data) + 3
data = [0] + data + [V]
d = set(data)
m = len(data)
c = [0] * m
v = 0

c[-1] = 1
for i in reversed(range(0, m - 1)):
    c[i] = sum(c[j] for j in range(i + 1, min(i + 4, m)) if data[j] - data[i] <= 3)

print(c[0])
