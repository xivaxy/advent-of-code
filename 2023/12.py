from aocd import data, submit
from aocd.models import Puzzle
import numpy as np
from functools import cache
from aoc_utils import intify, neigh4, neigh8

ans=0
s='''???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1'''
# data=s

@cache
def dfs(row, pos, remaining_groups: list) -> int:
    """Count the number of possible arrangements of adjacent groups of #s in row[pos:]. 
    ? in row are wildcards can be # or .
    remaining_groups is the list of lengths of groups that have not been placed yet, in the correct order.
    """
    if len(remaining_groups)==0:
        if all(c in '.?' for c in row[pos:]):
            return 1
        return 0
    if pos+sum(remaining_groups)+len(remaining_groups)-1>len(row):
        return 0
    res = 0
    if row[pos] in '.?':
        res+=dfs(row, pos+1, remaining_groups)
    if row[pos]=='.':
        return res
    l = remaining_groups[0]
    if all(row[pos+i] in "#?" for i in range(l)) and (pos+l==len(row) or row[pos+l] in '.?'):
        res+=dfs(row, pos+l+1, remaining_groups[1:])
    return res

for line in data.splitlines():
    row, nums=line.split()
    pattern = intify(nums)[0]
    cnt=dfs("?".join([row]*5), 0, tuple(pattern*5))
    ans+=cnt

print(ans)
# submit(ans)