import sys
sys.setrecursionlimit(10**7)

def dfs(x, y):
    global count
    graph[x][y] = 0
    count += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
            dfs(nx, ny)

n, m = map(int, input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
graph = []
result = []
max_paint_size = 0
for _ in range(n):
    graph.append(list(map(int, input().split())))
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            count = 0
            dfs(i, j)
            result.append(count)
if len(result) == 0:
    print(0)
    print(0)
else:
    print(len(result))
    print(max(result))
