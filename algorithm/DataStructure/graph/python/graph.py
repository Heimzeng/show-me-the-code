class Graph(object):
    """docstring for Graph"""
    def __init__(self, V):
        self.V = V
        self.E = 0
        self.adj = [[] for i in range(V)]  # adj table
        # self.adj =                       # adj matrix
    def V(self):
        return self.V
    def E(self):
        return self.E
    def addEdge(self, v, w):  # no arrow Graph
        if w not in self.adj[v]:
            self.adj[v].append(w)
        if v not in self.adj[w]:
            self.adj[w].append(v)
        self.E += 1
    def adj(self, v):
        return self.adj[v]
    def DFS(self, v):
        self.marked = [False for i in range(self.V)]
        self.parent = [-1 for i in range(self.V)]
        self.__dfsWithWhile(v)
    def __dfs(self, v):
        self.marked[v] = True
        for w in self.adj[v]:
            if not self.marked[w]:
                self.parent[w] = v
                self.__dfs(w)
    def __dfsWithWhile(self, v):
        stack = []
        stack.append(v)
        self.marked[v] = True
        while len(stack) > 0:
            cur = stack.pop()
            for w in self.adj[cur]:
                if not self.marked[w]:
                    stack.append(w)
                    self.marked[w] = True
                    self.parent[w] = cur
                    break # important !
    def BFS(self, v):
        self.marked = [False for i in range(self.V)]
        self.parent = [-1 for i in range(self.V)]
        self.__bfs(v)
    def __bfs(self, v):
        queue = []
        queue.append(v)
        self.marked[v] = True
        while len(queue) > 0:
            cur = queue.pop(0)
            for w in self.adj[cur]:
                if not self.marked[w]:
                    queue.append(w)
                    self.marked[w] = True
                    self.parent[w] = cur
    def hasPathTo(self, v):
        return self.marked[v]
    def pathTo(self, v):
        path = []
        x = v
        while x != 0:
            path.insert(0, x)
            x = self.parent[x]
        path.insert(0, 0)
        return path
    '''
    if use stack without marked list, we will get all paths
    but if with marked, we just visit every vertice once, so we may can not get all paths(at most time)
    '''
    def getCircles(self, node):
        self.stack = []
        self.circles = []
        self.__getCircles(node)
        return self.circles
    
    def __getCircles(self, node):
        self.stack.append(node)
        for neibor in self.adj[node]:
            if neibor not in self.stack:
                self.__getCircles(neibor)
            else:
                index = self.stack.index(neibor)
                circle = self.stack[index:] + [self.stack[index]]
                if circle not in self.circles:
                    self.circles.append(circle)
        self.stack.pop(-1)
    def getShortestPath(self, v, w):
        paths = self.getPaths(v, w)
        shortestpath = []
        for path in paths:
            if len(shortestpath) == 0:
                shortestpath = path
            elif len(path) < len(shortestpath):
                shortestpath = path
        return shortestpath
    def getPaths(self, v, w):
        self.stack = []
        self.paths = []
        self.__getPaths(v, w)
        return self.paths
    def __getPaths(self, v, w):
        self.stack.append(v)
        for neibor in self.adj[v]:
            if neibor == w:
                self.paths.append(self.stack + [neibor])
            elif neibor not in self.stack:
                self.__getPaths(neibor, w)
        self.stack.pop(-1)

class Digraph(object):  # test pass 20190309
    """docstring for Digraph"""
    def __init__(self, V, hotelTimes):
        self.V = V
        self.E = 0
        self.adjTable = [[] for _ in range(V)]  # adj table
        self.adjMatrix = [[0 for _ in range(V)] for _ in range(V)]  # adj matrix
        # self.hotelTimes = [0 for _ in range(V)]
        self.hotelTimes = hotelTimes
    def V():
        return self.V
    def E():
        return self.E
    def adj(self, v):
        return self.adjTable[v]
    def addEdge(self, v, w, weight=1):
        self.adjTable[v].append(w)
        self.adjMatrix[v][w] = weight   # weights are only recorded in adj matrix
        self.E += 1
    def dijkstra(self, S, needPath=False, longest=False):  # needPath was deprecated
        if longest:
            d = [float('-inf') for _ in range(self.V)]
        else:
            d = [float('inf') for _ in range(self.V)]
        d[S] = self.hotelTimes[S]
        previous = [None for _ in range(self.V)]
        S = []
        Q = [i for i in range(self.V)]
        while len(Q) > 0:   # main body of dijkstra algorithm
            u = -1
            if longest:
                # u = d.index(max([d[i] for i in Q])) # will result in error
                maxTemp = float('-inf')
                for i in Q:
                    if d[i] > maxTemp:
                        u = i
                        maxTemp = d[i] 
            else:
                # u = d.index(min([d[i] for i in Q])) # maybe there is a better way to get u
                minTemp = float('-inf')
                for i in Q:
                    if d[i] < minTemp:
                        u = i
                        maxTemp = d[i] 
            if u == -1:
                break
            Q.remove(u)
            S.append(u)
            for e in self.adjTable[u]:
                if longest:
                    if self.adjMatrix[u][e] + d[u] + self.hotelTimes[e] > d[e]:
                        d[e] = self.adjMatrix[u][e] + d[u] + self.hotelTimes[e]
                        previous[e] = u
                else:
                    if self.adjMatrix[u][e] + d[u] + self.hotelTimes[e] < d[e]:
                        d[e] = self.adjMatrix[u][e] + d[u] + self.hotelTimes[e]
                        previous[e] = u
        return d, previous
    def getAllPath(self):
        paths = []
        if self.E == 0:
            return paths
        S = [False for i in range(self.V)]
        while False in S:
            f = S.index(False)
            stack = [f]
            Q = [f]
            while len(stack) > 0:
                cur = stack[-1]
                S[cur] = True
                if len(self.adjTable[cur]) == 0:
                    paths.append(stack.copy()) # copy cannot be ignored!
                    stack.pop()
                    continue
                flag = False
                for adjPoint in self.adjTable[cur]:
                    if adjPoint not in Q:
                        Q.append(adjPoint)
                        stack.append(adjPoint)
                        flag = True # 这都能忘了写？
                        break
                if flag == False:
                    stack.pop()
                    for adjPoint in self.adjTable[cur]:
                        if adjPoint in Q:
                            Q.remove(adjPoint)
        return paths
    '''
    def reverse(self):
        Digraph R(self.V)
        for v in range(self.V):
            for w in self.adj(v):
                R.addEdge(w, v)
        return R
    '''
if __name__ == '__main__':
    ''' test about undirected graph
    graph = Graph(5)
    with open('graph.txt', 'r') as f:
        for line in f:
            v, w = line.split(' ')
            graph.addEdge(int(v), int(w))
    graph.addEdge(4, 4)
    graph.DFS(0)
    print(graph.marked)
    print(graph.adj)
    print(graph.getCircles(0))
    print(graph.getPaths(1, 3))
    print(graph.getPaths(3, 3))
    print(graph.getShortestPath(3, 1))
    print("hasPathTo4: ", graph.hasPathTo(3))
    print("pathTo4: ", graph.pathTo(3))
    graph.BFS(0)
    print("hasPathTo4: ", graph.hasPathTo(3))
    print("pathTo4: ", graph.pathTo(3))
    '''
    # test about directed graph
    digraph = Digraph(5, [3, 2, 10, 5, 7])
    with open('input.txt', 'r') as f:
        for line in f:
            v, w, e = line.split(' ')
            digraph.addEdge(int(v), int(w), int(e))
    d, p = digraph.dijkstra(0, False, True)
    print(d)
    print(p)
    print(digraph.getAllPath())