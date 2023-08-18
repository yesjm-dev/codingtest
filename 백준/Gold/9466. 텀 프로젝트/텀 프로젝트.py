import sys

sys.setrecursionlimit(10**7)
input = sys.stdin.readline


def dfs(x):
    global result
    visited[x] = True
    cycle.append(x)
    num = graph[x]

    if visited[num]:
        if num in cycle:
            result += cycle[cycle.index(num) :]
        return
    else:
        dfs(num)


t = int(input())
for _ in range(t):
    n = int(input())
    graph = [0] + list(map(int, input().split()))
    visited = [False] * (n + 1)
    result = []

    for i in range(1, n + 1):
        if not visited[i]:
            cycle = []
            dfs(i)
    print(n - len(result))
