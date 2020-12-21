# memory game

ns = [15, 5, 1, 4, 7, 0]
nsd = {x: i for i, x in enumerate(ns[:-1])}
n = len(ns)
last = ns[-1]

for i in range(n, 2020):
    x = (i-1 - nsd[last]) if last in nsd else 0
    nsd[last] = i-1
    last = x

print(last)
