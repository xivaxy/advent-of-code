from aocd import data, lines, numbers, submit
import numpy as np
import re

from aoc_utils import intify, neigh4


dots = [re.match(r"(\d+),(\d+)", l).groups() for l in data.split("\n\n")[0].split()]
inst = [re.match(r"fold along ([xy])=(\d+)", l).groups() for l in data.split("\n\n")[1].split("\n")]

print(intify(dots[:5]))

