from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 1
    while queue:
        x, y = queue.popleft()
        if x == bx and y == by:
            return graph[bx][by] - 1
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < l and 0 <= ny < l and graph[nx][ny] == 0:
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1


tc = int(input())
dx = [+2, +1, -1, -2, -2, -1, +1, +2]
dy = [+1, +2, +2, +1, -1, -2, -2, -1]
for _ in range(tc):
    l = int(input())
    ax, ay = map(int, input().split())
    bx, by = map(int, input().split())
    graph = [[0] * l for _ in range(l)]
    print(bfs(ax, ay))
