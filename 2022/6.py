from collections import Counter
import sys
from aocd import data, lines, numbers, submit
import numpy as np
cnt = Counter(data[:14])
for i in range(14, len(data)+1):
    if all(c<=1 for k, c in cnt.items()):
        submit(i)
        sys.exit()
    cnt[data[i-14]]-=1
    cnt.update(data[i:i+1])
