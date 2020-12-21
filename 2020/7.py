# shiny gold bags
from common import INPUT_DIR
from collections import defaultdict

data = []
with open(f"{INPUT_DIR}\\7.txt") as f:
    data = f.read().strip()

n = len(data)
res = 0
content = {}
containers = defaultdict(list)
start = " bags contain "
for l in data.splitlines():
    head = l[: l.index(start)]
    cont = [p.strip() for p in l[l.index(start) + len(start) : -1].split(",")]
    if cont[0].startswith("no"):
        content[head] = []
    else:
        content[head] = [
            (s[s.index(" ") + 1 : s.index(" bag")], int(s[: s.index(" ")]))
            for s in cont
        ]
        for nam, cnt in content[head]:
            containers[nam].append((head, cnt))

visited = set()
nodes = ["shiny gold"]
res = 0

while len(nodes) > 0:
    node = nodes.pop()
    for h, cnt in containers[node]:
        if h not in visited:
            visited.add(h)
            nodes.append(h)

print(len(visited))


def dfs(bag):
    if len(content[bag]) == 0:
        return 1
    res = 0
    for h, cnt in content[bag]:
        res += cnt * dfs(h)
    return res + 1


print(dfs("shiny gold") - 1)
