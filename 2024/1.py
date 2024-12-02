from aocd import data, submit
import re, sys
sys.path.append('../advent-of-code')
from aoc_utils import intify, neigh4, neigh8

print(intify(data)[:5])

lines = data.split('\n')
ans = 0
a,b = [], {}
for line in lines:
    x,y = line.split('   ')
    x = int(x)
    y = int(y)
    a.append(x)
    if y not in b:
        b[y] = 1
    else:  
        b[y] += 1

# a.sort()
# b.sort()
for i in range(len(a)):
    ans += a[i] * b.get(a[i], 0)

# print(ans)
# submit(ans)
