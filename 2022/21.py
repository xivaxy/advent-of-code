from aocd import data, lines, numbers, submit
import numpy as np
import re
import sys
from aoc_utils import intify, neigh4, neigh8

# djpv: psrp * gzbq
m = {l.split(":")[0]: l.split(": ")[1] for l in lines}
for k in m:
    if " " in m[k]:
        a,op,b = m[k].split(" ")
        m[k] = (a, op, b)
    # else:
    #     m[k] = int(m[k])

def dfs(st):
    if st=='humn':
        return 'x'
    if isinstance(m[st], str):
        return m[st]
    elif st!='root':
        a,op,b = m[st]
        return str(int(eval(dfs(a)+op+dfs(b))))
    else:
        a,op,b = m[st]
        # print(dfs(a))
        print(dfs(b))

ch = {
    "+":"-",
    "-":"+",
    "*":"/",
    "/":"*",
     }

# def eq(s, val):
#     if s=='humn':
#         print("answer",val)
#         # submit(val)
#         sys.exit()
#     try:
#         a,op,b = m[s]
#     except:
#         print("wrong eq call", s, m[s])
#         sys.exit()
#     try:
#         a = dfs(a)
#     except:
#         b = dfs(b)
#         match op:
#             case '+': val_a = str(eval(val+'-'+b))
#             case '-': val_a = str(eval(val+'+'+b))
#             case '*': 
#                 assert eval(val+'/'+b)==int(eval(val+'/'+b)), f"{s}->{m[s]}, {val}, {b}, {eval(val+'/'+b)}"
#                 val_a = str(int(eval(val+'/'+b)))
#             case '/': val_a = str(eval(val+'*'+b))
#         print(f"{s}->{m[s]} wants to be {val}, {b=}, hence {val_a}")
#         eq(a, val_a)
#     else:
#         match op:
#             case '+': val_b = str(eval(val+'-'+a))
#             case '-': val_b = str(eval(val+'+'+a))
#             case '*': 
#                 assert int(eval(val+'/'+a))==(eval(val+'/'+a))
#                 val_b = str(int(eval(val+'/'+a)))
#             case '/': 
#                 assert int(eval(a+'/'+val))==(eval(a+'/'+val))
#                 val_b = str(int(eval(a+'/'+val)))
#         print(f"{s}->{m[s]} wants to be {val}, {a=}, hence {val_b}")
#         eq(b, val_b)

def eq(s, val):
    if not isinstance(val, int):
        val = float(val)
        assert val==int(val)
        val = int(val)
    if s=='humn':
        print("answer", val)
        sys.exit()
    a,op,b=m[s]
    nota = False
    try:
        a = dfs(a)
    except:
        nota=True
    if nota:
        b = dfs(b)
        eq(a, eval(str(val)+ch[op]+b))
    else:
        if op not in '-/':
            eq(b, eval(str(val)+ch[op]+a))
        else:
            eq(b, eval(a+op+str(val)))
        


# root: hsdb + mwrd
eq("hsdb", "34588563455325")
# print(dfs("mwrd"))
# print(ans)
# submit(ans) 