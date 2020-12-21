# 
from common import INPUT_DIR
import os
from collections import defaultdict

DAY = os.path.basename(__file__)[:-3]
input_path = f"{INPUT_DIR}\\{DAY}.txt"

with open(input_path) as f:
    data = f.read().strip().splitlines()
    n = len(data)
    print(f"Read {n} lines from {input_path}")

res = 0

