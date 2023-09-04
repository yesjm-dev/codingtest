from collections import deque


def bfs():
    queue = deque()
    queue.append((home_x, home_y))
    while queue:
        x, y = queue.popleft()
        if abs(x - festival_x) + abs(y - festival_y) <= 1000:
            print("happy")
            return
        for i in range(n):
            if not visited[i]:
                nx, ny = graph[i]
                if abs(x - nx) + abs(y - ny) <= 1000:
                    visited[i] = True
                    queue.append((nx, ny))
    print("sad")
    return


t = int(input())
for _ in range(t):
    n = int(input())
    graph = []
    home_x, home_y = map(int, input().split())
    for _ in range(n):
        x, y = map(int, input().split())
        graph.append((x, y))
    festival_x, festival_y = map(int, input().split())
    visited = [False for _ in range(n + 1)]
    bfs()