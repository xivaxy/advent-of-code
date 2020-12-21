# Handheld Halting
from common import INPUT_DIR
import os

DAY = os.path.basename(__file__)[:-3]
input_path = f"{INPUT_DIR}\\{DAY}.txt"

with open(input_path) as f:
    print(f"reading {input_path}")
    data = f.read().strip().splitlines()
    n = len(data)


def run(data2):
    res = 0
    visited = []
    ptr = 0
    while ptr not in visited and ptr != n:
        ins = data2[ptr]
        visited.append(ptr)
        if ins.startswith("nop"):
            ptr += 1
        elif ins.startswith("acc"):
            res += int(ins.split(" ")[1])
            ptr += 1
        elif ins.startswith("jmp"):
            ptr += int(ins.split(" ")[1])
    return ptr, res, visited


ptr, res, visited0 = run(data)
print(f"Final acc {res}")
print(f"visited {len(visited0)} ops")

for i in range(n):
    if data[i].startswith("jmp"):
        data2 = data.copy()
        data2[i] = data2[i].replace("jmp", "nop")
    elif data[i].startswith("nop"):
        data2 = data.copy()
        data2[i] = data2[i].replace("nop", "jmp")
    else:
        continue

    ptr, res, visited = run(data2)

    if ptr == n:
        for j, (a, b) in enumerate(zip(visited0, visited)):
            if a != b:
                break

        print(f"Correct final acc {res}")
        print(f"visited {len(visited)} ops, op #{j} diverged")
        print(
            f"last common: line {visited[j-1]}: {data2[visited[j-1]]}, {data[visited0[j-1]]}"
        )
        print(
            f"next: new line {b} {data2[visited[j]]}, old line {a} {data[visited0[j]]}"
        )
        break
