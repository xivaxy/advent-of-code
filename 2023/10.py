from aocd import data, submit
from aocd.models import Puzzle
import numpy as np
import re, sys
from aoc_utils import intify, neigh4, neigh8

ans=0
# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
# The pipe that contains the animal is one large, continuous loop.

s='''FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L'''
directions_start = [(-1, 0), (0, -1)]
directions_map = {"|": [(1,0), (-1,0)], "-": [(0,1), (0,-1)], "L": [(0,1), (-1,0)], "F": [(1,0), (0,1)], "7": [(0,-1), (1,0)], "J": [(-1,0), (0,-1)]}

# data=s
# directions_start = [(0, -1), (1,0)]

start_letter = next(k for k,v in directions_map.items() if v==directions_start)
maze = data.splitlines()
w,h = len(maze[0]), len(maze)
start = data.replace('\n','').index('S')//w, data.replace('\n','').index('S')%w

def step(pos, direction):
    return pos[0]+direction[0], pos[1]+direction[1]

visited = [start, step(start, directions_start[0])]
while True:
    cur = visited[-1]
    for direction in directions_map[maze[cur[0]][cur[1]]]:
        if (nxt:=step(cur, direction))!=visited[-2]:
            break
    else:
        raise
    if nxt==start:
        # ans1 = len(visited)//2
        break
    visited.append(nxt)

contour = [["."]*w for _ in range(h)]
for pos in visited:
    contour[pos[0]][pos[1]] = maze[pos[0]][pos[1]]
contour[start[0]][start[1]] = start_letter

for line in contour:
    print("".join(line))

for i in range(h):
    intersection_even = True
    for j in range(min(w, h)):
        if i+j>=h:
            break
        if contour[i+j][j] in "|-JF":
            intersection_even = not intersection_even
        elif contour[i+j][j]=="." and not intersection_even:
            ans+=1

for i in range(1, w):
    intersection_even = True
    for j in range(min(w, h)):
        if i+j>=w:
            break
        if contour[j][i+j] in "|-JF":
            intersection_even = not intersection_even
        elif contour[j][i+j]=="." and not intersection_even:
            ans+=1

print(ans)
submit(ans)