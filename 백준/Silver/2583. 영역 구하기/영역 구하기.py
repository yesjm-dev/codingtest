import sys
sys.setrecursionlimit(10000)


def dfs(x, y, count):
    graph[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < m) and (0 <= ny < n) and graph[nx][ny] == 0:
            count = dfs(nx, ny, count + 1)
    return count


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

m, n, k = map(int, input().split(" "))
graph = [[0] * n for _ in range(m)]
result = []
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split(" "))
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            result.append(dfs(i, j, 1))
print(len(result))
print(*sorted(result))