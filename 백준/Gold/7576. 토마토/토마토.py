from collections import deque

def bfs():
    while queue:
        qx, qy = queue.popleft()
        for i in range(4):
            nx = qx + dx[i]
            ny = qy + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                queue.append((nx, ny))
                graph[nx][ny] = graph[qx][qy] + 1


m, n = map(int, input().split())
graph = []
queue = deque()
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
result = 0
for _ in range(n):
    graph.append(list(map(int, input().split())))
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i, j))
bfs()
for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    result = max(result, max(i))
print(result - 1)