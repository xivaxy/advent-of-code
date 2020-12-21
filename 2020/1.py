from common import INPUT_DIR

data = []

with open(f"{INPUT_DIR}\\1.txt") as f:
    for line in f:
        line = line.strip()
        data.append(line)

n = len(data)
print(len(data))
res = 0

s = set([0])
i = 0
while True:
    l = data[i]
    res += int(l)
    if res in s:
        print(res)
        break
    s.add(res)
    i = (i + 1) % n

# print(res)
