# XMAS-encrypted list of numbers
from common import INPUT_DIR
import os
from collections import defaultdict

DAY = os.path.basename(__file__)[:-3]
input_path = f"{INPUT_DIR}\\{DAY}.txt"

with open(input_path) as f:
    data = f.read().strip().splitlines()
    n = len(data)
    print(f"Read {n} lines from {input_path}")

res = 0
nw = True
content = {}
containers = defaultdict(list)
rr = 3

data = [int(d) for d in data]

prev = data[:25]
bad = 0
# bad = 2089807806

for i in range(25, n):
    if data[i] not in (prev[j] + prev[k] for j in range(25) for k in range(j, 25)):
        print(data[i])
        bad = data[i]

    prev = prev[1:] + [data[i]]

for i in range(n):
    for j in range(i + 2, n):
        test = sum(data[i:j])
        if test == bad:
            print(i, j)
            print(min(data[i:j]) + max(data[i:j]))
