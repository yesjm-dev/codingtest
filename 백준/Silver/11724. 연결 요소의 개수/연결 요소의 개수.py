def dfs(x):
    visited[x] = True

    for node in graph[x]:
        if not visited[node]:
            dfs(node)

n, m = map(int, input().split(" "))
graph = [[] for _ in range(n + 1)]
count = 0
visited = [False] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split(" "))
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)