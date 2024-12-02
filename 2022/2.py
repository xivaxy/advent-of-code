from aocd import data, lines, numbers, submit
import numpy as np

# A for Rock, B for Paper, and C for Scissors
# in response: X for Rock, Y for Paper, and Z for Scissors. Winning every time would be suspicious, so the responses must have been carefully chosen.
# shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won)
# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"

rs = [l.split() for l in lines]
a2b = {"A":'X', "B": "Y", "C":"Z"}
sc = {'X': 1, "Y": 2, "Z":3}
m = {'X': {'A': 3, 'B': 1, 'C': 2},
'Y': {'A': 1, 'B': 2, 'C': 3},
'Z': {'A': 2, 'B': 3, 'C': 1}}
s = 0
for a,b in rs:
    # s+=sc[b]
    # aa = a2b[a]
    match b:
        case 'X': s+=m[b][a]
        case 'Y': s+=m[b][a]+3
        case 'Z': s+=m[b][a]+6
submit(s)