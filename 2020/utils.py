from collections import defaultdict

data0 = """a:b,a:c,a:d,b:c,b:d,c:d,c:e,d:f,e:f,e:g,f:g"""
data3 = """a:b,a:c,a:d,b:c,b:d,c:d,c:e,d:f,e:f,e:b,f:g,x:y,y:x,z:z"""

g = defaultdict(list)
for d in data0.split(","):
    k, v = d.split(":")
    g[k].append(v)
    g[v]
g = dict(g)


def cycles(g):
    vis = set()
    cur = []
    curs = set()
    res = []
    sorting = []

    def dfs(n):
        cur.append(n)
        curs.add(n)
        for v in g[n]:
            if v in vis:
                continue
            if v in curs:
                res.append(cur[cur.index(v):])
            else:
                dfs(v)
        cur.pop()
        curs.remove(n)
        vis.add(n)
        sorting.append(n)

    for n in g:
        if n not in vis:
            dfs(n)

    return res, sorting[::-1]


print(cycles(g))
