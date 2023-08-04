def dfs(x, y, count):
    global result
    result = max(result, count)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not graph[nx][ny] in alphas:
            alphas.add(graph[nx][ny])
            dfs(nx, ny, count + 1)
            alphas.remove(graph[nx][ny])

n, m = map(int, input().split(" "))
graph = []
result = 0
alphas = set()
for _ in range(n):
    graph.append(list(input()))

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
alphas.add(graph[0][0])
dfs(0, 0, 1)
print(result)