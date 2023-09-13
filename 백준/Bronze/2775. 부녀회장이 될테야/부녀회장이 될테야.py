t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())
    cache = [i for i in range(1, n + 1)]
    for i in range(k):
        for j in range(1, n):
            cache[j] += cache[j - 1]
    print(cache[-1])