import sys
sys.setrecursionlimit(10**9)

def dfs(x, y, color):
    if n <= x or x < 0 or n <= y or y < 0:
        return False
    if graph[x][y] == color and not visited[x][y]:
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny, color)
        return True
    return False


n = int(input())
graph = []
result_1 = 0
result_2 = 0
count = 0
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
colors = ["R", "G", "B"]

for _ in range(n):
    graph.append(list(map(str, input())))

visited = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        for c in colors:
            if dfs(i, j, c):
                result_1 += 1

for i in range(n):
    for j in range(n):
        if graph[i][j] == "G":
            graph[i][j] = "R"

visited = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        for c in colors:
            if dfs(i, j, c):
                result_2 += 1

print(result_1, result_2)