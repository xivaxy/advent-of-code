# Monster Messages (Recursive string matching)
from common import INPUT_DIR
import os
from itertools import product, chain

DAY = os.path.basename(__file__)[:-3]
input_path = f"{INPUT_DIR}\\{DAY}.txt"

with open(input_path) as f:
    data = f.read().strip()

rules, msgs = data.split("\n\n")
msgs = msgs.splitlines()
rd = {int(r.split(":")[0]): list(map(lambda x: x.strip().split(" "),
                                     r.split(":")[1].split("|"))) for r in rules.strip().splitlines()}
for k, v in rd.items():
    rd[k] = [list(map(lambda x: x[1] if x[0] == '"' else int(x), l))
             for l in v]


cache = {}


def dfs(x):
    if x in cache:
        return cache[x]
    if isinstance(rd[x][0][0], str):
        res = set(rd[x][0][0])
    else:
        res = set(chain(
            *[map(lambda t: "".join(t), product(*[dfs(z) for z in li])) for li in rd[x]]))
    cache[x] = res
    return res


print("Part1:", sum(1 for m in msgs if m in dfs(0)))


# 8: 42 | 42 8
# 11: 42 31 | 42 11 31

def check(m):
    # 8 = len(cache[i]) for i = 8,42,31
    for i in range(1, 1 + len(m)//8):
        for j in range(1, 1 + len(m)//8):
            if i*8 + j*16 != len(m):
                continue
            ind31 = 8*(i+j)
            if (all(m[k*8:(k+1)*8] in cache[8] for k in range(i+j)) and
                    all(m[ind31+k*8:ind31+(k+1)*8] in cache[31] for k in range(j))):
                return True
    return False


print("Part2:", sum(1 for m in msgs if check(m)))
