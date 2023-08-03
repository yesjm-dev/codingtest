import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x):
    visited[x] = True
    for node in graph[x]:
        if not visited[node]:
            dfs(node)
            result[node] = x

n = int(input())
graph = [[] for _ in range(n + 1)]
result = [None for i in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(n - 1):
    a, b = map(int, input().split(" "))
    graph[a].append(b)
    graph[b].append(a)

dfs(1)

for i in range(2, n + 1):
    print(result[i])
