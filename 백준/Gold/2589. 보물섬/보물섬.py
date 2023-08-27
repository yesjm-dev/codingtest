from collections import deque


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    max_ = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
                if graph[nx][ny] == "L":
                    queue.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
                    max_ = max(max_, visited[nx][ny])
    return max_ - 1


n, m = map(int, input().split())
graph = [list(str(input())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == "L":
            visited = [[0] * m for _ in range(n)]
            result = max(result, bfs(i, j))
print(result)