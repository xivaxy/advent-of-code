import sys
from aocd import data, lines, numbers, submit
import numpy as np

nums = numbers[0]
nb = (len(numbers)-1)/5
assert int(nb)==nb
nb = int(nb)
boards = np.array([numbers[1+i*5:6+i*5] for i in range(nb)], dtype=int)
marks = np.zeros_like(boards)
won = set()
for n in nums:
    marks[boards==n]=1
    done = False
    for b in range(nb):
        if b in won:
            continue
        for i in range(5):
            if np.all(marks[b, i, :]==1) or np.all(marks[b, :, i]==1):
                won.add(b)
                if len(won)==nb:
                    submit(n*boards[b][marks[b]==0].sum(), "b")
                    sys.exit()
                done = True
                break

                # submit(n*boards[b][marks[b]==0].sum(), "a")