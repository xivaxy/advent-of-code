from aocd import data, lines, numbers, submit
import numpy as np
import re
import sys
# from aoc_utils import intify, neigh4, neigh8

dat = """1
2
-3
3
-2
0
4
-100
200"""

MUL = 811589153

nums = [(n*MUL, i) for i, n in enumerate([int(l) for l in data.splitlines()])]
N = len(nums)
# print(N, "Numbers")
i = 0
zz = None
for t in range(10):
    print(f"time {t}")
    # moved=set()
    for j in range(N):
        if j>0 and j%1000==0:
            print(f"moving {j}-th")
        for i in range(N):
            if nums[i][1]==j:
                break
        n= nums[i][0]
        if n==0:
            zz = j
            # i+=1
            # moved.add(j)
        else:
            del nums[i]
            ind = i + n
            if ind>0:
                ind%=(N-1)
            else:
                ind%=(N-1)
                if ind==0:
                    ind=N-1
            nums.insert(ind, (n, j))
            # moved.add(j)
            # if ind<=i:
            #     i+=1

# print(nums)
# print("Moved", len(moved))
# if len(moved)<N:
#     for i in range(N):
#         if i not in moved:
#             print(data.splitlines()[i], i, "not moved")
#             sys.exit()
zind = nums.index((0, zz))
i = zind
ans = 0
i+=1000
i%=N
# print(nums[i][0])
ans+=nums[i][0]
i+=1000
i%=N
# print(nums[i][0])
ans+=nums[i][0]
i+=1000
i%=N
# print(nums[i][0])
ans+=nums[i][0]
print("Total", ans)
submit(ans)
