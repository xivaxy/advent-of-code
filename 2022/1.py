from aocd import data, lines, numbers, submit
import numpy as np

elves = [[int(l) for l in e.split()] for e in data.split("\n\n")]
submit(max([sum(e) for e in elves]))
submit(sum(sorted([sum(e) for e in elves])[-3:]))