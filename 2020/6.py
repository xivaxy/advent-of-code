# Customs questions
from common import INPUT_DIR
from functional import seq

data = []
with open(f"{INPUT_DIR}\\6.txt") as f:
    data = f.read().strip()

n = len(data)
res = 0
for l in data.split("\n\n"):
    res += len(seq(l.split("\n")).map(lambda x: set(x)).reduce(lambda x, y: x.union(y)))

print(res)
