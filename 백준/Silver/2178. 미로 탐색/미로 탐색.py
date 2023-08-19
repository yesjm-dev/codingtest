from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1
    return graph[n - 1][m - 1]


n, m = map(int, input().split())
graph = []
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
for _ in range(n):
    graph.append(list(map(int, input())))

print(bfs(0, 0))
