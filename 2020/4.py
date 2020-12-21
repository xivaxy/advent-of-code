# Passport Processing
from common import INPUT_DIR
import re

data = []
with open(f"{INPUT_DIR}\\4.txt") as f:
    for line in f:
        line = line.strip()
        data.append(line)

n = len(data)
print(len(data))
res = 0

fs = set(
    [
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid",
    ]
)


def valid(d: dict):
    if not fs.issubset(set(d.keys())):
        return False
    return (
        1920 <= int(d["byr"]) <= 2002
        and 2010 <= int(d["iyr"]) <= 2020
        and 2020 <= int(d["eyr"]) <= 2030
        and (
            d["hgt"][-2:] == "cm"
            and 150 <= int(d["hgt"][:-2]) <= 193
            or d["hgt"][-2:] == "in"
            and 59 <= int(d["hgt"][:-2]) <= 76
        )
        and re.match(r"^#[0-9a-f]{6}$", d["hcl"]) is not None
        and (d["ecl"] in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"))
        and re.match(r"^[0-9]{9}$", d["pid"]) is not None
    )


s = dict()
for i, l in enumerate(data):
    if i == n - 1:
        s.update(x.split(":") for x in l.split(" "))
    if l == "" or i == n - 1:
        # print(s)
        if valid(s):
            res += 1
        s = dict()
    else:
        s.update(x.split(":") for x in l.split(" "))

print(res)
