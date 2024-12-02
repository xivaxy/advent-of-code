from aocd import data, submit
from aocd.models import Puzzle
import numpy as np
import regex as re  # third-party regex module that supports overlapping matches
import sys
from aoc_utils import intify, neigh4, neigh8

lines = data.split('\n')
ans = 0
# for line in lines:
#     first_digit = [c for c in line if c.isdigit()][0]
#     last_digit = [c for c in line if c.isdigit()][-1]
#     ans+=int(first_digit+last_digit)

# lines = """26sevenseven3twonelq""".splitlines()

words = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
pattern = re.compile(r'(' + '|'.join(words.keys()) + "|" + '|'.join(words.values()) + r')')
print(pattern)
for line in lines:
    matches = pattern.findall(line, overlapped=True)
    first_digit = matches[0]
    if len(first_digit)>1:
        first_digit = words[first_digit]
    last_digit = matches[-1]
    if len(last_digit)>1:
        last_digit = words[last_digit]
    ans+=int(first_digit+last_digit)

print(ans)
submit(ans)