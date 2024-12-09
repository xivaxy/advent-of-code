from aocd import data, submit
import networkx as nx

s='''47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47'''
test = False
if test:
    data=s
ans=0

d1,d2=data.split('\n\n')
edges = [
    tuple(map(int, x.split('|')))
    for x in d1.split('\n')
]
paths = [
    list(map(int, x.split(',')))
    for x in d2.split('\n')
]

G = nx.DiGraph()
G.add_edges_from(edges)
for path in paths:
    H = G.subgraph(path)
    for i in range(len(path)-1):
        if nx.has_path(H, path[i+1], path[i]):
            break
    else:
        continue
        # ans+=path[(len(path)-1)//2]
    correct_path = list(nx.topological_sort(H))
    ans += correct_path[(len(correct_path)-1)//2]

print(ans)
if not test:
    submit(ans)