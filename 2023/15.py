from aocd import data, submit
from aocd.models import Puzzle
import numpy as np
import re, sys
from aoc_utils import intify, neigh4, neigh8

# Determine the ASCII code for the current character of the string.
# Increase the current value by the ASCII code you just determined.
# Set the current value to itself multiplied by 17.
# Set the current value to the remainder of dividing itself by 256.

ans=0
s='''rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'''
# data=s
steps = data.strip().split(',')
def HASH(s):
    h=0
    for c in s:
        h = (h + ord(c)) * 17
        h = h % 256
    return h

# ans = sum(HASH(s) for s in steps)

boxes = [{} for i in range(256)]
for s in steps:
    l = s.replace('-','=').split('=')[0]
    box = HASH(l)
    if "-" in s:
        boxes[box].pop(l, 0)
    else:
        boxes[box][l] = int(s.split('=')[1])

for i in range(256):
    for j, (k,v) in enumerate(boxes[i].items()):
        ans += (i+1)*(j+1)*v

print(ans)
submit(ans)