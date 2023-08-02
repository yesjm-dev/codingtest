def dfs(x, depth):
    global arrive
    if depth == 5:
        arrive = True
        return
    visited[x] = True
    for node in graph[x]:
        if not visited[node]:
            dfs(node, depth + 1)
    visited[x] = False # 제일 깊게 탐색했다가 빠져나오는것이기 때문에 방문 표시 해제

n, m = map(int, input().split(" "))
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
arrive = False

for _ in range(m):
    a, b = map(int, input().split(" "))
    graph[a].append(b)
    graph[b].append(a)

for i in range(n):
    dfs(i, 1)
    if arrive:
        break
if arrive:
    print("1")
else:
    print("0")