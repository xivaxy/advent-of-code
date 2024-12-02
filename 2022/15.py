from aocd import data, lines, numbers, submit
import numpy as np
import re
import sys
from aoc_utils import intify
import bisect

dat = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""

a = np.array(intify([re.match(r"Sensor at x\=(-?\d+), y\=(-?\d+): closest beacon is at x\=(-?\d+), y\=(-?\d+)", l).groups() for l in data.splitlines()]), dtype=int)
b = a[:, :2]
c = a[:, 2:]
n = a.shape[0]
MAX=4000000
# MAX=20
for target in range(0, MAX+1):
    if target%10000==0:
        print(target)
    segments = []
    for i in range(n):
        dist = np.abs(b[i]-c[i]).sum()
        ydist=abs(target-b[i,1])
        xdist = (dist-ydist)
        if xdist>=0:
            x_seg = [b[i,0]-xdist, b[i,0]+xdist]
            # if c[i][1]==target:
                # if x_seg[0]==x_seg[1]:
                #     continue
                # if x_seg[0]==c[i][0]:
                #     x_seg[0]+=1
                # elif x_seg[1]==c[i][0]:
                #     x_seg[1]-=1
                # else:
                #     raise
            bisect.insort(segments, tuple(x_seg))

    segments = intify(segments)
    segments_merged = []
    seg = segments[0]
    for s in segments[1:]:
        if s[0]<=seg[1]+1:
            seg[1] = max(s[1], seg[1])
        else:
            segments_merged.append(seg)
            seg = s
    segments_merged.append(seg)
    cnt=0
    segments_final = []
    for s in segments_merged:
        if s[1]<0 or s[0]>MAX:
            continue
        cnt+=min(MAX, s[1]) - max(0, s[0]) + 1
        segments_final.append((max(0, s[0]), min(MAX, s[1])))
    if cnt==MAX:
        print(target)
        print(segments_final)
        if len(segments_final)==2:
            x=segments_final[0][1]+1
            ans = MAX*x+target
            print(ans)
            submit(ans)
            sys.exit()
        else:
            raise
# submit(ans)
