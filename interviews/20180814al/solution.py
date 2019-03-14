import sys
sys.path.append("../../")
from algorithm.DataStructure.graph.graph import Digraph

N, M = input().split(' ')
N = int(N)
M = int(M)
hotelTimes = []
for _ in range(N):
    hotelTimes.append(int(input()))
g = Digraph(N, hotelTimes)
for _ in range(M):
    a, b = input().split(' ')
    g.addEdge(int(a)-1, int(b)-1, 0)

maxd = [0]
relaPrevious = []
for i in range(N):
    d, p = g.dijkstra(i, False, True)
    if max(d) > max(maxd):
        maxd = d
        relaPrevious = p
m = max(maxd)

paths = g.getAllPath()
print(len(paths), m)