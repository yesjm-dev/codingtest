n = int(input())
d = []
for _ in range(n):
    d.append(input().split())
d.sort(key=lambda x: int(x[0]))
for i in d:
    print(i[0], i[1])