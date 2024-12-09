from aocd import data, submit
import sys
sys.path.append('../advent-of-code')
from aoc_utils import intify, neigh4, neigh8, tuple_add, tuple_sub

s='''....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...'''
test = False
if test:
    data=s
ans=0

lines = data.split('\n')
m = len(lines)
n = len(lines[0])
locs = [[-1 if c=='#' else 0 for c in row] for row in lines]
start_i = data.replace("\n", "").index('^')
x,y = start_i//n, start_i%n
start = x, y
print(m,n, x,y)
swne = neigh4
d = 2  # north
# locs[x][y] = 2  # visited
# while True:
#     x+=swne[d][0]
#     y+=swne[d][1]
#     if x<0 or x>=m or y<0 or y>=n:
#         break
#     if locs[x][y]==-1: # wall
#         x-=swne[d][0]
#         y-=swne[d][1]
#         d = (d+1)%4
#     else:
#         locs[x][y] = 2

# for i in range(m):
#     ans+=locs[i].count(2)

def print_locs(limx=100, limy=100):
    for i in range(min(m, limx)):
        for j in range(min(n, limy)):
            if locs[i][j]==-1:
                print('#', end='')
            elif locs[i][j]==0:
                print(' ', end='')
            elif locs[i][j]==-2:
                print('O', end='')
            else:
                print('.', end='')
                # print(hex(locs[i][j])[2], end='')
        print()
    print()


def move(xy, d):
    nxt=tuple_add(xy, swne[d])
    if not (0<=nxt[0]<m and 0<=nxt[1]<n):
        return (False, d)
    if locs[nxt[0]][nxt[1]]<0:
        d = (d+1)%4
        return (xy, d)
    return (nxt, d)

def walk(xy, d):
    walked = {(xy, d)}
    while True:
        xy, d = move(xy, d)
        if not xy:
            return False
        if (xy, d) in walked:
            return True
        walked.add((xy, d))

blocks = set()
visited = {start}

while True:
    nxt, d = move((x,y), d)
    if not nxt:
        break
    if nxt!=(x,y) and (nxt not in blocks) and nxt not in visited:
        # can try a block
        locs[nxt[0]][nxt[1]] = -2
        d1 = (d+1)%4
        if walk((x,y), d1):
            blocks.add(nxt)
            ans+=1
        locs[nxt[0]][nxt[1]] = 0
    visited.add(nxt)
    x, y = nxt

assert ans == len(blocks)
print(ans)
if not test:
    submit(ans)