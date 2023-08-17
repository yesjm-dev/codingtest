import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline


def dfs(x, group):
    global result
    if result:
        return
    visited[x] = group

    for i in graph[x]:
        if not visited[i]:
            dfs(i, -group)
        elif visited[x] == visited[i]:
            result = True
            return


t = int(input())
for _ in range(t):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    visited = [False] * (v + 1)
    result = False
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, v + 1):
        if not visited[i]:
            dfs(i, 1)
            if result:
                break

    if result:
        print("NO")
    else:
        print("YES")
