import numpy as np

f = open("b")
caves = {}

def has_double(path):
    for i in range(len(path)):
        p = path[i]
        if p.islower() and p in path[i+1:]:
            return True
    return False


for l in f:
    parts = l[:-1].split("-")
    if parts[0] not in caves:
        caves[parts[0]] = []
    caves[parts[0]].append(parts[1])
    if parts[1] not in caves:
        caves[parts[1]] = []
    caves[parts[1]].append(parts[0])


paths = [["start"]]
finished_paths = []
#print(caves)

while len(paths) > 0:
    new_paths = []
    for p in paths:
        #print (p)
        if p[-1] not in caves:
            continue
        outs = caves[p[-1]]
        for out in outs:
            if out == "start":
                continue
            if out.islower() and out in p and has_double(p):
                continue
            if out == "end":
                new_p = p[:]
                new_p.append("end")
                finished_paths.append(new_p)
                continue
            new_p = p[:]
            new_p.append(out)
            new_paths.append(new_p)
    paths = new_paths[:]


print(finished_paths)
print(len(finished_paths))