from aocd import data, submit
from aocd.models import Puzzle
import numpy as np
import re, sys, math
from aoc_utils import intify, neigh4, neigh8
from z3 import Solver, Ints

# tags: geometry, 3d, line intersection
# part2 is impossible to solve by hand, but easy with z3

ans=0
s='''19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3'''
# x, y, z @ vx, vy, vz
# x,y,z - position of this rock at t=0
# vx, vy, vz - constant velocity of this rock
MIN = 10000000000000
MAX = 500000000000000
MAXV = 1000
test = False
if test:
    MIN = 7
    MAX = 27
    MAXV=10
    data=s
pos = []
v = []
for l in data.splitlines():
    x, y, z, vx, vy, vz = map(int, re.findall(r'-?\d+', l))
    pos.append(np.array((x, y, z), dtype=np.int64))
    v.append(np.array((vx, vy, vz), dtype=np.int64))

N = len(pos)
for i in range(0):
    for j in range(i+1, 0):
        # dist = np.linalg.norm(pos[i][:2] - pos[j][:2])
        # dist2 = np.linalg.norm(pos[i][:2]+v[i][:2] - pos[j][:2]-v[j][:2])
        if v[i][1] == v[j][1]:
            continue
            dpos = pos[i] - pos[j]
            if np.cross(dpos[:2], v[i][:2]) == 0:
                # todo: fix logic later
                pass
        # find intersection point
        # y = (x-pos[i][0]) * v[i][1] + pos[i][1]
        # same for j
        x_inter = (pos[j][1] - pos[i][1] - v[j][1]*pos[j][0] + v[i][1]*pos[i][0]) / (v[i][1] - v[j][1])
        y_inter = (x_inter-pos[i][0]) * v[i][1] + pos[i][1]
        # sign of a number
        math.copysign
        
        if MIN<=x_inter<=MAX and MIN<=y_inter<=MAX and (x_inter-pos[i][0])*np.sign(v[i][2])>=0 and (x_inter-pos[j][0])*np.sign(v[j][2])>=0:
            ans+=1
            # print(i, j, x_inter, y_inter)

# find the 3d line such that all rocks trajectories intersect it
            
def costf(x,y,z, vx, vy, vz):
    # x,y,z, vx, vy, vz = arg
    res = 0
    for i in range(N):
        res += np.linalg.norm(np.dot(np.cross((vx, vy, vz), v[i]), pos[i]-(x,y,z)) )**2
    return res

s = Solver()
x,y,z, vx, vy, vz, t1, t2 = Ints('x y z vx vy vz t1 t2')
s.add(x>=MIN, x<=MAX, y>=MIN, y<=MAX, z>=MIN, z<=MAX, vx>=-MAXV, vx<=MAXV, vy>=-MAXV, vy<=MAXV, vz>=-MAXV, vz<=MAXV, t1>0, t2>0)
s.add(vx*vx+vy*vy+vz*vz>0)

# line intersection condition:
# np.dot(np.cross((vx, vy, vz), v[i]), pos[i]-(x,y,z)) == 0
for i in range(N):
    s.add( (pos[i][0]-x)*(vy*v[i][2]-vz*v[i][1]) + (pos[i][1]-y)*(vz*v[i][0]-vx*v[i][2]) + (pos[i][2]-z)*(vx*v[i][1]-vy*v[i][0]) == 0 )
    
# for i in range(3):
s.add(x + vx*t1 == pos[0][0] + v[0][0]*t1)
s.add(y + vy*t1 == pos[0][1] + v[0][1]*t1)
s.add(z + vz*t1 == pos[0][2] + v[0][2]*t1)
s.add(x + vx*t2 == pos[1][0] + v[1][0]*t2)
s.add(y + vy*t2 == pos[1][1] + v[1][1]*t2)
s.add(z + vz*t2 == pos[1][2] + v[1][2]*t2)


print(s.check())
m = s.model()
arg0 = [m[x].as_long(), m[y].as_long(), m[z].as_long(), m[vx].as_long(), m[vy].as_long(), m[vz].as_long()]
print(arg0)
print(costf(*arg0))
t1, t2 = m[t1].as_long(), m[t2].as_long()
print(t1, t2)
ans = sum(arg0[:3])

# print(loss((24, 13, 10, -3, 1, 2)))

print(ans)
if not test:
    submit(ans)