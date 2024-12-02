from aocd import data, submit
from aocd.models import Puzzle
import numpy as np
import re, sys
from aoc_utils import intify, neigh4, neigh8
from bisect import bisect
ans = 0

# seeds: range_start range_len range_start range_len ...
# source category-to-destination category map:
# dest_start src_start length

s="""seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

# data = s

seeds = [int(x) for x in data.splitlines()[0].split(": ")[1].split()]
seeds = [(seeds[i], seeds[i+1]) for i in range(0, len(seeds), 2)]

maps = data.split("\n\n")[1:]
for mp in maps:
    mp = mp.splitlines()[1:]
    m = []
    for line in mp:
        line = [int(x) for x in line.split()]
        dest_start, src_start, length = line
        m.append((src_start, dest_start, length))
    m.sort()
    seeds2 = []
    for seed_start, seed_len in seeds:
        first_seed_idx = bisect(m, (seed_start+1, ))
        last_seed_idx = bisect(m, (seed_start+seed_len+1, ))
        for idx in range(first_seed_idx, last_seed_idx+1):
            if idx>0:
                src_start, dest_start, length = m[idx-1]
                mapped_start = dest_start+max(seed_start-src_start, 0)
                mapped_end = dest_start+min(seed_start+seed_len-src_start, length)
                if mapped_start < mapped_end:
                    seeds2.append((mapped_start, mapped_end-mapped_start))
                unmapped_start = max(src_start+length, seed_start)
                unmapped_end = seed_start+seed_len
                if idx<len(m):
                    unmapped_end = min(unmapped_end, m[idx][0])
                if unmapped_start < unmapped_end:
                    seeds2.append((unmapped_start, unmapped_end-unmapped_start))
            else:
                unmapped_start = seed_start
                unmapped_end = min(seed_start+seed_len, m[0][0])
                if unmapped_start < unmapped_end:
                    seeds2.append((unmapped_start, unmapped_end-unmapped_start))
    seeds = seeds2

ans, _ = min(seeds)

print(ans)
submit(ans)