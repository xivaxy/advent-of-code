from aocd import data, submit
from aocd.models import Puzzle
import numpy as np
import re, sys
from aoc_utils import intify, neigh4, neigh8
import networkx as nx
import matplotlib
import matplotlib.pyplot as plt

# tags: graph, connected components, minimum edge cut, networkx
# hard to solve by hand, but easy with networkx

ans=0
s='''jqt: rhn xhk nvd
rsh: frs pzl lsr
xhk: hfx
cmg: qnr nvd lhk bvb
rhn: xhk bvb hfx
bvb: xhk hfx
pzl: lsr hfx nvd
qnr: nvd
ntq: jqt hfx bvb xhk
nvd: lhk
lsr: lhk
rzs: qnr cmg lsr rsh
frs: qnr lhk lsr'''
test = False
if test:
    data=s
G = nx.Graph()
for l in data.splitlines():
    st, nb = l.split(': ')
    for n in nb.split():
        G.add_edge(st, n)
# fig = plt.figure()
# nx.draw(G, with_labels=True, ax=fig.add_subplot(111))
# fig.savefig("graph.png")
# edges_to_remove = [("scr", "klj"), ("sdv", "mxv"), ("gqr", "vbk")]
mincut = nx.minimum_edge_cut(G)
G.remove_edges_from(mincut)
# #count the sizes of the two connected components
cc1, cc2 = nx.connected_components(G)
ans = len(cc1) * len(cc2)

print(ans)
if not test:
    # submit(ans)
    pass