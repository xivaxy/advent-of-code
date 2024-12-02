from aocd import data, lines, numbers, submit
import numpy as np

# packets = data.split("\n\n")
# ps = [(eval(p.split("\n")[0]), eval(p.split("\n")[1])) for p in packets]
ps = [eval(l) for l in lines if l]
ans = 0

def wrong(l1, l2):
    if isinstance(l1, int):
        if isinstance(l2, int):
            if l1>l2:
                return 1
            elif l1==l2:
                return 0
            else:
                return -1
        return wrong([l1], l2)
    if isinstance(l2, int):
        return wrong(l1, [l2])
    for a1, a2 in zip(l1, l2):
        f=wrong(a1, a2)
        if f!=0:
            return f
    return wrong(len(l1),len(l2))

# for i, (p1, p2) in enumerate(ps):
#     if wrong(p1, p2)!=1:
#         ans+=i+1

from functools import cmp_to_key

ps.extend(([[2]], [[6]] ))
ps.sort(key=cmp_to_key(wrong))
i1 = ps.index([[2]])
i2 = ps.index([[6]])
submit((i1+1)*(i2+1))