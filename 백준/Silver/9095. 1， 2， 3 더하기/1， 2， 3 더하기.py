t = int(input())
cache = dict()
cache[1] = 1
cache[2] = 2
cache[3] = 4
for i in range(4, 12):
    cache[i] = cache[i - 1] + cache[i - 2] + cache[i - 3]
for _ in range(t):
    n = int(input())
    print(cache[n])