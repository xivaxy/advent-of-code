from aocd import data, lines, numbers, submit
import numpy as np

from aoc_utils import neigh4

kn = 10
r = np.zeros((kn, 2), dtype=int)
vis = set([(0,0)])
dirs = "RDLU"
for l in lines:
    d, cnt = l.split()
    cnt = int(cnt)
    d = neigh4[dirs.index(d)]
    for i in range(cnt):
        r[0] += d
        h = r[0]
        for ki in range(1, kn):
            t = r[ki]
            if (dif:=np.abs(t-h)).max()>=2:
                if 0 in dif:
                    t[:] = (t+h)//2
                elif dif[1]==1:
                    t[1] = h[1]
                    t[:] = (t+h)//2
                elif dif[0]==1:
                    t[0] = h[0]
                    t[:] = (t+h)//2
                elif dif.tolist() == [2,2]:
                    t[:] = (t+h)//2
                else:
                    print(l, r, ki, h, t)
                    raise
            h = t
        vis.add(tuple(r[-1]))

print(len(vis))
submit(len(vis))