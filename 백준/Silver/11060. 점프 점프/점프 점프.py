from collections import deque

def bfs(x):
    queue = deque()
    queue.append(x)

    while queue:
        q = queue.popleft()
        if q + graph[q - 1] >= n:
            return visited[q] + 1
        for i in range(1, graph[q - 1] + 1):
            nq = q + i
            if visited[nq] == 0:
                queue.append(nq)
                visited[nq] = visited[q] + 1
    else:
        return -1

n = int(input())
graph = list(map(int, input().split()))
visited = [0] * (n + 1)

if n == 1:
    print(0)
else:
    print(bfs(1))