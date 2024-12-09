from aocd import data, submit

s='''190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20'''
test = False
if test:
    data=s
ans=0
lines = data.split('\n')
res = [int(l.split(": ")[0]) for l in lines]
vals = [list(map(int, l.split(": ")[1].split())) for l in lines]

def dfs(r,val,cum,i):
    if i==len(val):
        if cum==r:
            return True
        return False
    if cum>r:
        return False
    if dfs(r,val,cum+val[i],i+1):
        return True
    if dfs(r,val,cum*val[i],i+1):
        return True
    if dfs(r,val,int(str(cum)+str(val[i])),i+1):
        return True
    return False

for i in range(len(res)):
    if dfs(res[i],vals[i],vals[i][0],1):
        ans+=res[i]

print(ans)
if not test:
    submit(ans)