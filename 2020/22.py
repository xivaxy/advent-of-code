# 2 player card game with recursive sub-games
from common import INPUT_DIR
import os
from collections import deque
from threading import Event, Thread

DAY = os.path.basename(__file__)[:-3]
input_path = f"{INPUT_DIR}\\{DAY}.txt"

with open(input_path) as f:
    data = f.read().strip()

p1, p2 = data.split("\n\n")
p1 = list(map(int, p1.splitlines()[1:]))
p2 = list(map(int, p2.splitlines()[1:]))
n1, n2 = len(p1), len(p2)
d1 = deque(p1)
d2 = deque(p2)

gcache = {}


def play(d1, d2):
    global gcache
    cache = set()
    while True:
        tt = tuple(d1), tuple(d2)
        if tt in gcache:
            win = gcache[tt]
            break
        if tt in cache:
            win = 1
            break
        if len(d1) == 0:
            win = 2
            break
        if len(d2) == 0:
            win = 1
            break
        cache.add(tt)
        a1, a2 = d1.popleft(), d2.popleft()
        if a1 <= len(d1) and a2 <= len(d2):
            sub = play(deque(list(d1)[:a1]), deque(list(d2)[:a2]))
            if sub == 1:
                d1.extend((a1, a2))
            else:
                d2.extend((a2, a1))
        elif a1 > a2:
            d1.extend((a1, a2))
        elif a2 > a1:
            d2.extend((a2, a1))
        else:
            raise
    for tt in cache:
        gcache[tt] = win
    return win


def monitoring(interval: int = 1.0):
    stats = Event()

    def loop():
        cnt = 0
        while not stats.wait(interval):
            if len(gcache) > cnt:
                print(f"New {len(gcache)-cnt}, total {len(gcache)=}")
                cnt = len(gcache)

    Thread(target=loop, daemon=True).start()
    return stats


# to monitor the global cache size
monitoring()

win = play(d1, d2)
print(d1, d2)
if win == 1:
    w = d1
else:
    w = d2

print("Part2:", sum((i + 1) * c for i, c in enumerate(reversed(w))))
