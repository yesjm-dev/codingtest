from collections import deque


def bfs():
    while queue:
        qz, qx, qy = queue.popleft()
        for i in range(6):
            nx = qx + dx[i]
            ny = qy + dy[i]
            nz = qz + dz[i]
            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:
                if graph[nz][nx][ny] == 0:
                    queue.append((nz, nx, ny))
                    graph[nz][nx][ny] = graph[qz][qx][qy] + 1


m, n, h = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
queue = deque()
dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
result = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                queue.append((i, j, k))
bfs()
for i in graph:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        result = max(result, max(j))
print(result - 1)
