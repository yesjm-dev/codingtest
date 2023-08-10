import sys
sys.setrecursionlimit(100000)

def dfs(x, y, h):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (
            (0 <= nx < n)
            and (0 <= ny < n)
            and graph[nx][ny] > h
            and not visited[nx][ny]
        ):
            dfs(nx, ny, h)

n = int(input())
graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
for k in range(max(map(max, graph))):
    visited = [[False] * n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] > k and not visited[i][j]:
                dfs(i, j, k)
                count += 1
    result.append(count)
print(max(result))