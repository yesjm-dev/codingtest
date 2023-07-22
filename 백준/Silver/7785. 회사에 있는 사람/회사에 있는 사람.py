n = int(input())
d = {}
for _ in range(n):
    a,b = list(map(str, input().split()))
    d[a] = b
for key, value in sorted(d.items(), reverse=True):
    if value=='enter':
        print(key)