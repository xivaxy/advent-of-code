# Crab Cups (moving cups aroung the circle)
input = "467528193"

data = list(map(int, input))
m = len(data)
steps = 100
# Array-based
cur_ind = 0
for st in range(steps):
    cur = data[cur_ind]
    pick_pos = tuple(i % m for i in range(cur_ind + 1, cur_ind + 4))
    pick = [data[i % m] for i in pick_pos]
    dst = cur - 1
    if dst <= 0:
        dst = m
    while dst in pick:
        dst -= 1
        if dst <= 0:
            dst = m
    if pick_pos[-1] > pick_pos[0]:
        del data[pick_pos[0] : pick_pos[-1] + 1]
    else:
        del data[pick_pos[0] :]
        del data[: pick_pos[-1] + 1]
    ind2 = data.index(dst)
    data[ind2 + 1 : ind2 + 1] = pick
    cur_ind = (data.index(cur) + 1) % m

ind1 = (data.index(1) + 1) % m
res = []
while data[ind1] != 1:
    res.append(str(data[ind1]))
    ind1 = (ind1 + 1) % m

print("Part1", "".join(res))

data = list(map(int, input))
# Dict-based
steps = 10_000_000
cups = 1_000_000
pos = {n1: n2 for n1, n2 in zip(data, data[1:])}
pos[data[-1]] = 10
pos.update(((i, i + 1) for i in range(10, cups + 1)))
pos[cups] = data[0]

m = cups
c = data[0]

for st in range(steps):
    c1 = pos[c]
    c2 = pos[c1]
    c3 = pos[c2]
    c4 = pos[c3]
    dst = c - 1
    if dst <= 0:
        dst = m
    while dst == c1 or dst == c2 or dst == c3:
        dst -= 1
        if dst <= 0:
            dst = m
    dst2 = pos[dst]
    pos[c] = c4
    pos[dst] = c1
    pos[c3] = dst2
    c = pos[c]
    if st % 500000 == 0:
        print(st, end="\r")

r1 = pos[1]
r2 = pos[r1]
print("Part2", r1 * r2)
