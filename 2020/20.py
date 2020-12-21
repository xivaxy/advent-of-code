# Jurassic Jigsaw
from common import INPUT_DIR
import os
from collections import defaultdict
import numpy as np

DAY = os.path.basename(__file__)[:-3]
input_path = f"{INPUT_DIR}\\{DAY}.txt"

with open(input_path) as f:
    data = f.read().strip()
    n = len(data)
    print(f"Read {n} lines from {input_path}")

data = data.split("\n\n")
n = int(len(data)**0.5)
tiles = dict()
for tile in data:
    tile = tile.strip().splitlines()
    name = int(tile[0].split(" ")[1][:-1])
    tiles[name] = tile[1:]

m = len(tile[1:])


def std(s):
    if s <= s[::-1]:
        return s, False
    else:
        return s[::-1], True


tile_fps = dict()
fp_tile = defaultdict(list)
for name, t in tiles.items():
    fp = [t[0]]
    fp.append((t[i][-1] for i in range(m)))
    fp.append((reversed(t[-1])))
    fp.append((t[i][0] for i in reversed(range(m))))
    fp = [std("".join(f)) for f in fp]
    tile_fps[name] = fp
    for i, f in enumerate(fp):
        fp_tile[f[0]].append((name, i, f[1]))

fp_tile = dict(fp_tile)

g = defaultdict(set)
gext = defaultdict(set)
for fp, nodes in fp_tile.items():
    if len(nodes) >= 2:
        for x in nodes:
            for y in nodes:
                if y != x:
                    g[x[0]].add(y[0])
                    gext[x[0]].add((y[0], x, y))

g = dict(g)
gext = dict(gext)
degs = {}
res = 1
for x, v in g.items():
    degs[x] = len(v)
    if len(v) < 3:
        res *= x


print("Part1:", res)

start = 2953
cur = start
vis = set([cur])
# False means not flipped from the original
grid = [[(cur, False)]]
deg = 3
for i in range(n):
    deg0 = 4
    if i == 0 or i == n-1:
        deg0 -= 1
    for j in range(n):
        if i == 0 and j == 0:
            continue
        if j == n-1 or j == 0:
            deg = deg0 - 1
        else:
            deg = deg0
        for x in g[cur]:
            if degs[x] == deg:
                edge = next(filter(lambda z: z[0] == x, gext[cur]))
                if x in vis:
                    continue
                if i > 0 and (x not in g[grid[i-1][j][0]]):
                    continue
                # True means the same original side
                grid[-1].append((x, edge[1][2] != edge[2]
                                 [2], edge[1][1], edge[2][1]))
                vis.add(x)
                cur = x
                break
        else:
            raise
        if j == n-1:
            cur = grid[-1][0][0]
            if i != n-1:
                grid.append([])

edge = next(filter(lambda z: z[0] == grid[0][1][0], gext[start]))
grid[0][0] = (start, edge[1][2] == edge[2][2], edge[1][1], edge[2][1])

w = m-2
a = np.zeros((w*n, w*n), dtype=int)
curside = True
firstside = False
for i in range(n):
    for j in range(n):
        x = grid[i][j]
        t = np.array([[0 if c == "." else 1 for c in s[1:-1]]
                      for s in tiles[x[0]][1:-1]], dtype=int)
        if j == 0:
            trans = firstside if x[1] else not firstside
            firstside = trans
        else:
            trans = curside if x[1] else not curside
        curside = trans
        if trans:
            t = np.transpose(t)
        if j == 0:
            if i == 0:
                rot = x[2] - 1
            else:
                rot = 3-x[3] if trans else x[3]
        else:
            rot = -x[3] if trans else x[3]-3
        t = np.rot90(t, rot)
        a[w*i:w*(i+1), w*j:w*(j+1)] = t


pattern = """                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """
pattern = pattern.splitlines()
pattern = np.array([[0 if c == " " else 1 for c in s] for s in pattern])
# try varies rotation counts and transpose
pattern = np.rot90(pattern, 2)
# pattern = np.transpose(pattern)
monster_size = np.sum(pattern)
px, py = pattern.shape
nz = list(zip(*(np.nonzero(pattern))))

print(monster_size, np.sum(a))
for i in range(a.shape[0]-px):
    for j in range(a.shape[1]-py):
        if all(a[i+x, j+y] == 1 for x, y in nz):
            for x, y in nz:
                a[i+x, j+y] = 0

print("Part2:", np.sum(a))
