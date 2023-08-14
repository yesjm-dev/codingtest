import sys
sys.setrecursionlimit(10*6)

def dfs(x, weight):
    for a, b in graph[x]:
        if visited[a] == -1:
            visited[a] = weight + b
            dfs(a, visited[a])

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, input().split(" "))
    graph[a].append([b, c])
    graph[b].append([a, c])
for _ in range(m):
    d, e = map(int, input().split())
    visited = [-1] * (n + 1)
    visited[d] = 0
    dfs(d, 0)
    print(visited[e])