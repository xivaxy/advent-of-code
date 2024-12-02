from aocd import data, submit
from aocd.models import Puzzle
from collections import defaultdict
import numpy as np
import re, sys, math
from aoc_utils import intify, neigh4, neigh8

# tags: parsing, branching by numerical bounds conditions
# part2 requires merging of bounds and tree traversal

ans=0
# first workflows
# then cases
# each case starts in workflow "in"
# Example: px{a<2006:qkq,m>2090:A,rfg}, workflow named px, it first check is a<2006, if true, go to workflow qkq and execute it, if false, check if m>2090, if true, go to A, if false, go to rfg
# A means the case is accepted
# R means the case is rejected
s='''px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}'''
# data=s
wfs = {}
bounds = defaultdict(list)
cases = []
bounds_map = {"x": 0, "m": 1, "a": 2, "s": 3}
M = 4000
UB = [M+1]*4
LB = [0]*4

class Bounds:
    def __init__(self, ubs=UB, lbs=LB):
        self.ubs = ubs
        self.lbs = lbs
        self.empty = False
    
    def parse(condition: str):
        ubs = UB.copy()
        lbs = LB.copy()
        c = condition[0]
        sign = condition[1]
        bound = int(condition[2:])
        if sign=="<": ubs[bounds_map[c]] = bound
        else: lbs[bounds_map[c]] = bound
        return Bounds(ubs, lbs)

    def __repr__(self):
        return f"({self.ubs}, {self.lbs}, {self.empty})"
    
    def __hash__(self) -> int:
        if self.empty: return hash("empty")
        return hash((tuple(self.ubs), tuple(self.lbs)))
    
    def negate(self) -> "Bounds":
        ubs = UB.copy()
        lbs = LB.copy()
        to_split = False
        for i in range(4):
            if self.ubs[i]<=M: lbs[i] = self.ubs[i]-1
            if self.lbs[i]>0: 
                ubs[i] = self.lbs[i]+1
                if self.ubs[i]<=M: to_split = True
        if to_split:
            raise
            return [Bounds(ubs=ubs), Bounds(lbs=lbs)]
        else:
            return Bounds(ubs, lbs)

    def aand(self, other: "Bounds"):
        empty = False
        if self.empty or other.empty: empty = True
        ubs = UB.copy()
        lbs = LB.copy()
        for i in range(4):
            ubs[i] = min(self.ubs[i], other.ubs[i])
            lbs[i] = max(self.lbs[i], other.lbs[i])
            if ubs[i]-lbs[i]<=1: empty = True
        res = Bounds(ubs, lbs)
        if empty: res.empty = True
        return res
    
    def aand_list(self, others: list["Bounds"]):
        res = []
        for o in others:
            f = self.aand(o)
            res.append(f)
        return res
    
    def count(self):
        if self.empty: return 0
        res = 1
        for i in range(4):
            res*=self.ubs[i]-self.lbs[i]-1
        return res


for line in data.split('\n'):
    if line=='': break
    if line[0]=='{':
        # parse x,m,a,s
        x,m,a,s = line[1:-1].split(',')
        x,m,a,s = [ int(i.split("=")[1]) for i in [x,m,a,s] ]
        state = "in"
        print(x,m,a,s)
        cnt = 0
        while state!="A" and state!="R":
            rules = wfs[state]
            if cnt<5:
                print(state, rules)
                cnt+=1
            for r in rules:
                if type(r)==list:
                    if eval(r[0]):
                        state = r[1]
                        break
                else:
                    state = r
        if state=="A": ans+=(x+m+a+s)
    else:
        wf, rest = line.split('{')
        rules = rest.replace('}','').split(',')
        rules = [ r.split(':') if ":" in r else r for r in rules ]
        for r in rules:
            if type(r)==list:
                bounds[wf].append(Bounds.parse(r[0]))
        wfs[wf] = rules

def dfs(st, bound: Bounds|None) -> int:
    # returns the number of accepted cases for workflow st, when entering with bounds
    if bound.empty:
        return 0
    if st=="A": return bound.count()
    if st=="R": return 0
    rules = wfs[st]
    res = 0
    saved = Bounds()
    for i, r in enumerate(rules):
        if type(r)==list:
            _, nxt = r
            res+= dfs(nxt, bound.aand(saved).aand(bounds[st][i]))
            saved = saved.aand(bounds[st][i].negate())
        else:
            nxt = r
            res+= dfs(nxt, bound.aand(saved))
    return res

ans = dfs("in", Bounds())

print(ans)
# submit(ans)