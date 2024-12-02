import re
import sys
from aocd import data, lines, numbers, submit
import numpy as np

from aoc_utils import intify

# ans = 0
# nums = intify([re.match(r"(\d+)-(\d+),(\d+)-(\d+)",l).groups() for l in lines])
# for a1,b1,a2,b2 in nums:
#     # if (a1<=a2 and b1>=b2) or (a1>=a2 and b1<=b2):
#     if (a1 in range(a2,b2+1)) or (a2 in range(a1,b1+1)):
#         ans+=1

# submit(ans)

pairs = [tuple(map(int, pair.split('-'))) for line in lines for pair in line.strip().split(',')]
counter = 0
for a, b in pairs:
  # Check if range a fully contains range b
  if a[0] <= b[0] and a[1] >= b[1]:
    counter += 1
  # Check if range b fully contains range a
  elif b[0] <= a[0] and b[1] >= a[1]:
    counter += 1