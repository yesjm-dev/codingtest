import sys
sys.setrecursionlimit(10**9)

def dfs(x, weight):
    for a, b in graph[x]:
        if visited[a] == -1:
            visited[a] = weight + b # 이전 노드의 가중치 + 현재 노드의 가중치
            dfs(a, visited[a])


n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, input().split(" "))
    graph[a].append([b, c])
    graph[b].append([a, c])

visited = [-1] * (n + 1) # 탐색 확인 + 가중치 확인
visited[1] = 0 # 시작 노드의 가중치를 0으로 초기화
dfs(1, 0)

start = visited.index(max(visited)) # 찾은 노드에서 가장 먼 노드를 찾는다

visited = [-1] * (n + 1)
visited[start] = 0
dfs(start, 0)

print(max(visited))
