# Shuttle Search (Chinese Remainder Theorem)
from common import INPUT_DIR
import os
import math
from z3 import *

DAY = os.path.basename(__file__)[:-3]
input_path = f"{INPUT_DIR}\\{DAY}.txt"

with open(input_path) as f:
    data = f.read().strip().splitlines()
    n = len(data)
    print(f"Read {n} lines from {input_path}")

m = len(data[1])

T = int(data[0])
# data[1] = "17,x,13,19"
routes = [int(id) for id in data[1].split(",") if id != "x"]

t = T
while True:
    done = False
    for id in routes:
        if t % id == 0:
            print("Part1", (t-T)*id)
            done = True
            break
    if done:
        break
    t += 1

dataint = [int(id) if id != "x" else 0 for id in data[1].split(",")]
delays = {t: dataint.index(t) for t in routes}
rems = [(10*routes[i]-delays[routes[i]]) % routes[i] 
for i in range(len(routes))]

# Chinese RT
M=math.prod(routes)
Mk=[M//t for t in routes]
y=[pow(M//t, -1, t) for t in routes]
print("Part2:", sum(Mk[i]*y[i]*rems[i]
                    for i in range(len(routes))) % M)


# Sieve search - didn't work
# N = tt[0]
# r = N-d[tt[0]]
# # print(tt, d)

# for t in tt[1:]:
#     m = N
#     r = pow((t-d[t]) - r ), -1, N
#     while s%t!=:
#         s+=N
#     print("solved", t, d[t], s)
#     N*=t

# z3 SAT
N = len(routes)
N = 4
print(f"z3 SAT solver, {N} routes")
s = Solver()
t = Int("t")
s.add([t % routes[i] == rems[i] for i in range(N)] + [t>0])
s.check()
print(s.model())
