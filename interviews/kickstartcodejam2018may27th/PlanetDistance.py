import os

if __name__ == '__main__':  
    T = int(input())
    for _ in range(T):
        N = int(input())
        graph = [[] for i in range(N)]
        for __ in range(N):
            f, l = input().split(' ')
            f = int(f) - 1
            l = int(l) - 1
            graph[f].append(l)
            graph[l].append(f)
    print(graph)
    stack = []
    circles = []
    def DFS(node):
        stack.append(node)
        for nei in graph[node]:
            if nei not in stack:
                DFS(nei)
            elif nei != stack[-2]:
                circles.append(stack[stack.index(nei):] + [nei])
                #return (stack[stack.index(nei):] + [nei])
        stack.pop(-1)
    DFS(0)
    circle = circles[0]
    counts = [-1 for i in range(N)]
    stack = []
    def findcounts(node):
        if node in circle:
            counts[node] = 0
        else:
            stack.append(node)
            for nei in graph[node]:
                if nei not in stack and nei not in circle:
                    DFS(nei)
                elif nei in circle:
                    c = len(stack) 
                    if counts[node] == -1:
                        counts[node] = c
                    elif c < counts[node]:
                        counts[node] = c
            stack.pop(-1)
    for i in range(N):
        findcounts(i)
    print(counts)