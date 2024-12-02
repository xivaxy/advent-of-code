from aocd import data, lines, numbers, submit
import numpy as np
import bisect

ans = 0
cmds = data.split("\n$")
stack = []
dir_sizes = []
for cmd in cmds:
    lns = cmd.split("\n")
    cm = lns[0].lstrip("$ ")
    if cm.startswith("cd"):
        to = cm.split()[1]
        if to=='..':
            fd, sizes = stack.pop()
            total = sum(sizes.values())
            stack[-1][1][fd] = total
            dir_sizes.append(total)
        else:
            stack.append([to, {}])
    elif cm=='ls':
        for ln in lns[1:]:
            size, f = ln.split()
            stack[-1][1][f] = int(size) if size!='dir' else ""

while stack:
    fd, sizes = stack.pop()
    total = sum(sizes.values())
    if stack:
        stack[-1][1][fd] = total
    dir_sizes.append(total)

used = dir_sizes[-1]
left = 70000000 - used
need = 30000000
need_free = need - left
dir_sizes.sort()
ind = bisect.bisect_left(dir_sizes, need_free)

submit(dir_sizes[ind])
