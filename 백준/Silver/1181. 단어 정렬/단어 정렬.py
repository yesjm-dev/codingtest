n = int(input())
d = []
for _ in range(n):
    d.append(str(input()))
d = list(set(d))
d.sort()
d.sort(key=lambda x: len(x))
for i in d:
    print(i)