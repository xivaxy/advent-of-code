from aocd import data, submit
from aocd.models import Puzzle
import numpy as np
import re, sys
from aoc_utils import intify, neigh4, neigh8
from typing import Counter

ans=0
s='''32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483'''

# data=s
src = "AKQJT"
rep = "ZYX0V"

hand_types:dict[tuple, int] = { ():1, (2, ): 2, (2, 2): 3, (3, ): 4, (3, 2): 5, (4, ): 7, (5,): 8}

         
hands = []
for line in data.splitlines():
    hand, bid = line.split()
    # replace letter in hand from src to rep
    for i in range(len(src)):
        hand = hand.replace(src[i], rep[i])
    cnt = Counter(hand)
    typ = list(n for c, n in cnt.most_common() if n>1 and c!="0")
    if "0" in hand:
        if typ:
            typ[0]+=cnt["0"]
        elif len(cnt)>1:
            typ.append(cnt["0"]+1)
        else:
            typ.append(cnt["0"])
    typ = tuple(typ)
    hands.append((hand_types[typ],  hand, int(bid)))

hands.sort()
n = len(hands)
for i, (typ, hand, bid) in enumerate(hands):
    ans+=bid*(i+1)

print(ans)
submit(ans)