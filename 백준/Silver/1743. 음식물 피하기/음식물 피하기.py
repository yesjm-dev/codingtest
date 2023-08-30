from collections import deque


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 2
    max_ = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 < nx <= n and 0 < ny <= m and graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = 2
                max_ += 1
    return max_


n, m, k = map(int, input().split())
graph = [[0] * (m + 1) for _ in range(n + 1)]
result = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
for _ in range(k):
    r, c = map(int, input().split())
    graph[r][c] = 1
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if graph[i][j] == 1:
            result = max(result, bfs(i, j))
print(result)
