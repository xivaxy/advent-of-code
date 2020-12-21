# Operation Order
from common import INPUT_DIR
import os

DAY = os.path.basename(__file__)[:-3]
input_path = f"{INPUT_DIR}\\{DAY}.txt"

with open(input_path) as f:
    data = f.read().strip().splitlines()
    n = len(data)
    print(f"Read {n} lines from {input_path}")


data = [d.split(" ") for d in data]

res = 0

for d in data:
    x = 0
    op = "+"
    lev = 0
    stnum = []
    stop = []
    for t in d:
        if t.strip("()").isdecimal():
            while t.startswith("("):
                stnum.append(x)
                stop.append(op)
                x = 0
                op = "+"
                t = t[1:]
            y = int(t.strip(")"))
            x = x + y if op == "+" else x*y
            while t.endswith(")"):
                y = stnum.pop()
                op = stop.pop()
                x = x + y if op == "+" else x*y
                t = t[:-1]
        elif t in ("+", "*"):
            op = t
    res += x

print("Part1:", res)


res = 0
for d in data:
    z = 1
    x = 1
    op = "*"
    stack = []
    for t in d:
        if t.strip("()").isdecimal():
            while t.startswith("("):
                stack.append((z, x, op))
                z = x = 1
                op = "*"
                t = t[1:]

            y = int(t.strip(")"))
            if op == "+":
                x = x + y
            elif op == "*":
                z *= x
                x = y
            while t.endswith(")"):
                z *= x
                z0, x, op = stack.pop()
                if op == "+":
                    x += z
                elif op == "*":
                    z0 *= x
                    x = z
                z = z0
                t = t[:-1]
        elif t == "+":
            op = t
        elif t == "*":
            z *= x
            x = 1
            op = t
    z *= x
    res += z

print("Part2:", res)
