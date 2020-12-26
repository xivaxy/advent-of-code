# Combo Breaker (Diffie–Hellman key exchange)
from common import INPUT_DIR
import os

DAY = os.path.basename(__file__)[:-3]
input_path = f"{INPUT_DIR}\\{DAY}.txt"

with open(input_path) as f:
    data = f.read().strip().splitlines()

card = int(data[0])
door = int(data[1])
md = 20201227
n = 7
doorexp = 1
while n != card:
    n = (n * 7) % md
    doorexp += 1

print(f"{doorexp=}")
print("Part1:", pow(door, doorexp, md))
