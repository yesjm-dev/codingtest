# 플로이드-워셜 알고리즘 이용
# 각 정점에서 다른 모든 정점으로 연결됐는지 여부 확인
n, m = map(int, input().split())
graph = [[0] * n for _ in range(n)]
result = 0
for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] = 1
for i in range(n):
    count = 0
    for j in range(n):
        count += graph[i][j] + graph[j][i]
    if count == (n - 1):
        result += 1

print(result)