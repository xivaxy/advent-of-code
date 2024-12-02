from aocd import data, lines, numbers, submit
import numpy as np

from typing import Counter

ans = 0
n = len(lines)
for i in range(n//3):
    try:
        cmn = set(lines[3*i]).intersection(lines[3*i+1]).intersection(lines[3*i+2]).pop()
    except:
        print(lines[i:i+3])
        raise
    # n = len(l)
    # cmn  = set(l[:n//2]).intersection(l[n//2:]).pop()
    if ord(cmn) - ord('A') < 26:
        ans+=ord(cmn) - ord('A')+27
    else:
        ans+=ord(cmn) - ord('a')+1
submit(ans)