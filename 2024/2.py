from aocd import data, submit
import sys
sys.path.append('../advent-of-code')
from aoc_utils import intify

a = intify(data)
ans=0

def safe(b):
    for i in range(1,len(b)):
        if not 1<=b[i]-b[i-1]<=3:
            return 0
    else:
        return 1

for b in a:
    if b[0]>b[-1]:
        b = b[::-1]
    if b[0]<b[-1]:
        for i in range(0,len(b)):
            if safe(b[:i]+b[i+1:]):
                ans+=1
                break
    
print(ans)
submit(ans)