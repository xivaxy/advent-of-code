# Docking Data (bitmasked memory)
from common import INPUT_DIR
import os
import math
from collections import defaultdict

DAY = os.path.basename(__file__)[:-3]
input_path = f"{INPUT_DIR}\\{DAY}.txt"

with open(input_path) as f:
    data = f.read().strip().split("mask")
    n = len(data)
    print(f"Read {n} lines from {input_path}")

di = dict()

for d in data:
    if len(d)==0:
        continue
    l = d.strip().split("\n")
    if len(l)==0:
        continue
    m = l[0].strip()[2:]
    assert(len(m)==36)
    m0 = int(m.replace("X", "0"), 2)
    mx = sum(1 << (i-1) for i in range(1, len(m)+1) if m[-i] == "X")
    mxinv = sum(1 << (i-1) for i in range(1, len(m)+1) if m[-i] != "X")
    indx = [1<<(i-1) for i in range(1, len(m)+1) if m[-i] == "X"]
    keys = set()
    for i in range(2**len(indx)):
        r = 0
        for j in range(len(indx)):
            if i & (1<<j):
                r += indx[j]
        keys.add(r)

    assert(mx&m0==0)
    for v in l[1:]:
        v = v.strip()
        if len(v)==0:
            continue
        key = int(v.strip().split("[")[1].split("]")[0])
        value = int(v.strip().split("=")[1].strip())
        # di[key] = (value & mx ) | m0
        for k in keys:
            di[(key | m0) & mxinv | k] = value


print(sum(di[k] for k in di))
