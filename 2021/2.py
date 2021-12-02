from aocd import data, lines, submit

ans = 0

d = 0
h = 0
a = 0

for l in lines:
    c, n = l.split(" ")
    n = int(n)
    if c[0] == "f":
        h += n
        d += a * n
    elif c[0] == "d":
        a += n
    elif c[0] == "u":
        a -= n

ans = d * h

print(ans)
submit(ans)
