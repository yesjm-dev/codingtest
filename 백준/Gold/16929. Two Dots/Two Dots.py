import sys

n, m = map(int, input().split())
graph = [[p for p in sys.stdin.readline().strip()] for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
result = False

def dfs(x, y, count, color, sx, sy):
    global result
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if result is True:
            return
        if nx >= n or nx < 0 or ny >= m or ny < 0:
            continue
        if count >= 4 and sx == nx and sy == ny:
            result = True
            return True
        if not visited[nx][ny] and graph[nx][ny] == color:
            visited[nx][ny] = True
            dfs(nx, ny, count + 1, color, sx, sy)
            visited[nx][ny] = False
    return False


def solve():
    global result
    for i in range(n):
        for j in range(m):
            visited[i][j] = True
            dfs(i, j, 1, graph[i][j], i, j)
            if result:
                return "Yes"
    return "No"

print(solve())
