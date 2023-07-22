n,m = map(int, input().split())
d = {}
for _ in range(n):
    a = str(input())
    d[a] = 1
for _ in range(m):
    b = str(input())
    if d.get(b):
        d[b] = 2
d = dict(filter(lambda x: x[1]>1, d.items()))
print(len(d))
for i in sorted(d, reverse=False):
    print(i)