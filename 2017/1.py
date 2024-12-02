from aocd import data, submit
from aocd.models import Puzzle
import numpy as np
import re
import sys
from aoc_utils import intify, neigh4, neigh8

n = len(data)//2
ans = sum(int(c) for c,d in zip(data, data[n:] + data[:n]) if c == d)
print(ans)
submit(ans)
