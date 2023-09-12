n = int(input())
cache = [10000] * (n + 5)
cache[3] = 1
cache[5] = 1
for i in range(6, n + 1):
    cache[i] = min(cache[i - 3], cache[i - 5]) + 1
print(cache[n] if cache[n] < 10000 else -1)