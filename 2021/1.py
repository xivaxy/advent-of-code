from aocd import data, lines, numbers, submit
import math
import numpy as np

ans = 0

a = np.array(numbers)
ans = np.count_nonzero(a[1:] > a[:-1])
submit(ans)

b = np.convolve(a, [1, 1, 1], "valid")
ans = np.count_nonzero(b[1:] > b[:-1])

print(ans)
submit(ans)
