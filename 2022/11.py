from aocd import data, lines, numbers, submit
import numpy as np
from aoc_utils import intify

ms = data.split("\n\n")
tests = [int(m.split("\n")[3].split()[-1]) for m in ms]
goto = [(int(m.split("\n")[4].split()[-1]), int(m.split("\n")[5].split()[-1])) for m in ms]
items = [list(map(int, m.split("\n")[1].split(": ")[1].split(", "))) for m in ms]
ops =  intify([(m.split("\n")[2].split()[-2], m.split("\n")[2].split()[-1]) for m in ms])
print(items)
nm = 8
MOD = np.prod(tests)

cnts = [0]*nm
for i in range(10000):
    for m in range(nm):
        for w in items[m]:
            match ops[m][0]:
                case '+': w+=ops[m][1]
                case '*': w*=ops[m][1] if ops[m][1]!='old' else w
            w%=MOD
            items[goto[m][0 if w%tests[m]==0 else 1]].append(w)
            cnts[m]+=1
        items[m] = []
        

cnts.sort()
submit(cnts[-1]*cnts[-2])