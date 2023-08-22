from collections import deque

n, k = map(int, input().split())
visited = [-1] * 100001
dq = [1, -1, 2]

def bfs(x):
    queue = deque()
    queue.append(x)
    visited[x] = 0
    while queue:
        q = queue.popleft()
        for i in dq:
            nq = q * 2 if i == 2 else q + i
            if 0 <= nq <= 100000 and visited[nq] == -1:
                queue.append(nq)
                visited[nq] = visited[q] + 1
            if nq == k:
                return visited[nq]

print(bfs(n))