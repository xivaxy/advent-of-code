# Password policies
from common import INPUT_DIR
data = []

with open(f"{INPUT_DIR}\\2.txt") as f:
    for line in f:
        line = line.strip()
        data.append(line)

print(len(data))

result = 0
for line in data:
    num, ch, pw = line.split(" ")
    num1, num2 = num.split("-")
    num1 = int(num1)
    num2 = int(num2)
    ch = ch[0]
    cnt = 0
    # for c in pw:
    #     if c==ch:
    #         cnt+=1
    # if num1<=cnt<=num2:
    #     result += 1

    if len(pw) >= num1 and pw[num1 - 1] == ch:
        cnt += 1
    if len(pw) >= num2 and pw[num2 - 1] == ch:
        cnt += 1
    if cnt == 1:
        result += 1

print(result)
