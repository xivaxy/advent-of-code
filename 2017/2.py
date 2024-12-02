from aocd import data, submit
from aocd.models import Puzzle
import numpy as np
import re
import sys
from aoc_utils import intify, neigh4, neigh8
import itertools

lines = intify(data)
ans = sum(next(b//a for a,b in itertools.combinations(sorted(l), 2) if b % a == 0) for l in lines )

print(ans)
submit(ans)
