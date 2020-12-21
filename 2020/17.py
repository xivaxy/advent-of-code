# Conway Cubes
from common import INPUT_DIR
import os
import numpy as np
from itertools import product

DAY = os.path.basename(__file__)[:-3]
input_path = f"{INPUT_DIR}\\{DAY}.txt"

with open(input_path) as f:
    data = f.read().strip()

data = [list(map(int, d.replace("#", "1").replace(".", "0")))
        for d in data.splitlines()]
n = len(data)
CYC = 6
maxXY = n+2*CYC+1
maxZ = 2*CYC+1
a = np.zeros(shape=(maxXY, maxXY, maxZ, maxZ), dtype=int)
zero = (maxXY//2+1, maxZ//2+1)
a[zero[0]-n//2:zero[0]-n//2+n, zero[0]-n//2:zero[0]-n//2+n, zero[1], zero[1]] = data
aa = np.zeros_like(a)

for cyc in range(CYC):
    print(f"Cycle {cyc}")
    for coord in product(*map(range, a.shape)):
        cnt = 0
        for delta in product((-1, 0, 1), repeat=a.ndim):
            delta = np.array(delta)
            if not delta.any():
                continue
            coord2 = delta + coord
            # adding this sensible line makes the answer wrong
            # if (coord2 < 0).any():
            #     continue
            try:
                cnt += a[tuple(coord2)]
            except:
                pass
        if (a[coord] and 2 <= cnt <= 3) or cnt == 3:
            aa[coord] = 1
    a, aa = aa, a
    aa[:] = 0

print("Part2:", a.sum())
