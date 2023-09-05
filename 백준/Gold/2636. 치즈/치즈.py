from collections import deque


def bfs():
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = True
    count = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                elif graph[nx][ny] == 1:
                    visited[nx][ny] = True
                    graph[nx][ny] = 0
                    count += 1
    answer.append(count)
    return count


n, m = map(int, input().split())
graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
answer = []
time = 0
for _ in range(n):
    graph.append(list(map(int, input().split())))
while True:
    time += 1
    visited = [[False] * m for _ in range(n)]
    count = bfs()
    if count == 0:
        break
print(time - 1)
print(answer[-2])