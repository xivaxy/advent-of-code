# Binary Boarding
from common import INPUT_DIR
import re
from functional import seq

data = []
with open(f"{INPUT_DIR}\\5.txt") as f:
    data = f.read().strip()

n = len(data)
print(len(data))
res = 0
maxid = 0
p = []
ids = seq(data.splitlines()).map(
    lambda s: int(re.sub(r"[BR]", "1", re.sub(r"[FL]", "0", s)), 2)
)

idMax = ids.max()
idMin = ids.min()
print(idMax)
print(set(range(idMin, idMax + 1)).difference(ids))
