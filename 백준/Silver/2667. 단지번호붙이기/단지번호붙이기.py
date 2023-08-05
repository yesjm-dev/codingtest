def dfs(x, y):
    if n <= x or x < 0 or n <= y or y < 0:
        return False
    if graph[x][y] == 1:
        global count
        count += 1
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False


n = int(input())
graph = []
result = 0
num = []
count = 0
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for _ in range(n):
    graph.append(list(map(int, input())))

for i in range(n):
    for j in range(n):
        if dfs(i, j):
            num.append(count)
            result += 1
            count = 0
print(result)
num.sort()
for i in range(len(num)):
    print(num[i])
