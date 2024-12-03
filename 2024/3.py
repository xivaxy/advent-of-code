from aocd import data, submit
import re

s='''xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))'''
test = False
if test:
    data=s
ans=0

enabled = True
for line in data.split('\n'):
    # gs = re.findall(r'(?<=mul\()[0-9]{1,3},[0-9]{1,3}(?=\))', line)
    gs = re.findall(r'(do\(\)|don\'t\(\)|mul\([0-9]{1,3},[0-9]{1,3}\))', line)
    print(gs)
    for g in gs:
        print(g)
        if g.startswith('mul') and enabled:
            x,y = map(int, g[4:-1].split(','))
            ans+=x*y
        elif g=='do()':
            enabled = True
        elif g=="don't()":
            enabled = False

print(ans)
if not test:
    submit(ans)