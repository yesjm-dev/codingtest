def dfs(x):
    visited[x] = True

    for node in graph[x]:
        if not visited[node]:
            dfs(node)


n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
count = 0
visited = [False] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split(" "))
    graph[a].append(b)
    graph[b].append(a)

dfs(1)

print(visited.count(True) - 1)