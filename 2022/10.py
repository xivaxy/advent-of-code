from aocd import data, lines, numbers, submit
import numpy as np

inst = []
for l in lines:
    l = l.split()
    if len(l)==2:
        inst.append(int(l[1]))
    else:
        inst.append(None)

ans = 0
cyc = pos = 0
v = 1
# target = 20
crt = []
for ins in inst:
    crt.append('#' if abs(v-pos)<=1 else '.')
    cyc+=1
    pos = cyc%40
    if ins is not None:
        crt.append('#' if abs(v-pos)<=1 else '.')
        cyc+=1
        pos = cyc%40
        v += ins
        
for i in range(6):
    print("".join(crt[i*40:i*40+40]))

# submit("FBURHZCH")
