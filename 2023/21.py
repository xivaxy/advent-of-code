from aocd import data, submit
import numpy as np
from aoc_utils import intify, neigh4
from collections import defaultdict

# tags: game of life, bfs, infinite grid expansion, heuristic quadratic formula
# hard. Formula may be found with Wolfram Alpha

ans=0
s='''...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........'''
# data=s
a = data.split('\n')

h,w = len(a), len(a[0])
start = [i for i in range(h*w) if a[i//w][i%w]=='S'][0]
start = (start//w, start%w)

N=26501365
q_history = [1]
tc0 = {}  # tile counts
tc1 = {}
tc_history = defaultdict(list)
stable_tiles = {}
# M=5000
count_tiles = False
for i in range(0):
    nq = set()
    tc2 = defaultdict(int)
    for x,y in q:
        for dx,dy in neigh4:
            nx,ny = x+dx, y+dy
            if a[nx%h][ny%w]!='#':
                if count_tiles:
                    tile = nx//h, ny//w
                    if tile not in stable_tiles and (nx,ny) not in nq:
                        tc2[tile]+=1
                        nq.add((nx,ny))
                else:
                    nq.add((nx,ny))
    q = nq
    q_history.append(len(q))
    for t in tc2:
        if tc0.get(t,0)==tc2[t]:
            even, odd = tc1[t], tc2[t]
            if i%2==0:
                even, odd = odd, even
            stable_tiles[t] = (even, odd)
        tc_history[t].append(tc2[t])
    tc0 = tc1
    tc1 = tc2

d=None
dd=None

# lh = np.zeros((10, h), dtype=int)
q = {start}
cnt = 0
done = False
while True:
    d2 = np.zeros(h, dtype=int)
    for i in range(h):
        nq = set()
        for x,y in q:
            for dx,dy in neigh4:
                nx,ny = x+dx, y+dy
                if a[nx%h][ny%w]!='#':
                    nq.add((nx,ny))
        d2[i] = len(nq)-len(q)-cnt
        q = nq
        # lh[cnt//h, i] = len(q)
        cnt+=1
        if cnt%20==0:
            print(cnt)
    if not done:
        if d is not None:
            dd2 = d2-d
            if dd is not None:
                if np.all(dd2==dd):
                    done = True
                    count = cnt
                    leng = len(q)
                    diffs = d2
                    break
            dd = dd2
        d = d2

print(count, leng, diffs, dd)
# print(lh)

# size after cnt: len(q)
# size(cnt+1)= len(q)+d2[0]+cnt+dd[0]
# size(cnt+2)= size(cnt+1)+d2[1]+cnt+1+dd[1]
# size(cnt+h)= size(cnt)+sum(d2)+sum(dd)+sum(cnt+i for i in range(h)) = size(cnt)+sum(d2)+sum(dd) + h*(h-1)//2 + h*cnt
# size(cnt+h+1)= size(cnt+h)+d2[0]+2*dd[0] + h*(h-1)//2 + h*cnt + cnt+h
# size(cnt+h+2)= size(cnt+h)+sum(d2[:2])+2*sum(dd[:2])  + h*(h-1)//2 + h*cnt + cnt+h + cnt+h+1

def tri(n):
    return n*(n+1)//2

def size(n):
    epoch = (n-count)//h
    rem = n%h
    ans = leng + sum(diffs) * epoch + sum(dd) * tri(epoch)
    ans += sum(diffs[:rem]) + sum(dd[:rem])*(epoch+1)
    ans += tri(n-1)-tri(count-1)
    return ans

ans = size(N)
print(ans)
submit(ans)