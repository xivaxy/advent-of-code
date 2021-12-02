from aocd import data, lines, submit

ans = 0

d = 0
h = 0
a = 0

for l in lines:
    c, n = l.split(" ")
    n = int(n)
    match c[0]:
        case "f":
            h += n
            d += a * n
        case "d":
            a += n
        case "u":
            a -= n
            

ans = d * h

print(ans)
submit(ans)
