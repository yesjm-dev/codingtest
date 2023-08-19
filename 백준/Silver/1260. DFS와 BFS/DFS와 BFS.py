
from collections import deque
def dfs(x):
    visited[x] = True
    print(x, end=" ")
    for node in graph[x]:
        if not visited[node]:
            dfs(node)


def bfs(x):
    queue = deque([x])
    visited[x] = True
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()


visited = [False] * (n + 1)
dfs(v)
print()

visited = [False] * (n + 1)
bfs(v)