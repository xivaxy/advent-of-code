from aocd import data, lines, submit
import numpy as np

ans = 0

g = e = 0
m = len(lines[0])
r = 1
n = len(lines)
a = np.array([list(map(int, l)) for l in lines], np.int32)
s = np.sum(a, 0)
g = int("".join(map(str, (s > n / 2).astype(np.int32))), 2)
e = int("".join(map(str, (s < n / 2).astype(np.int32))), 2)
ans = g * e
submit(ans)

b = np.copy(a)
for i in range(m):
    nn = np.shape(b)[0]
    if nn == 1:
        break
    if np.sum(b[:, i]) >= nn / 2:
        most = 1
    else:
        most = 0
    b = b[b[:, i] == most]
p1 = int("".join(map(str, b[0, :])), 2)

b = np.copy(a)
for i in range(m):
    nn = np.shape(b)[0]
    if nn == 1:
        break
    if np.sum(b[:, i]) >= nn / 2:
        most = 0
    else:
        most = 1
    b = b[b[:, i] == most]
p2 = int("".join(map(str, b[0, :])), 2)
ans = p1 * p2

print(ans)
submit(ans)
