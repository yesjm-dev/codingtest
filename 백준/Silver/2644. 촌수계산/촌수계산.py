def dfs(x):
    visited[x] = True
    for node in graph[x]:
        if not visited[node]:
            result[node] = result[x] + 1
            dfs(node)


n = int(input())
a, b = map(int, input().split(" "))
m = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
result = [0] * (n + 1)
for _ in range(m):
    x, y = map(int, input().split(" "))
    graph[x].append(y)
    graph[y].append(x)

dfs(a)
if result[b] > 0:
    print(result[b])
else:
    print(-1)
