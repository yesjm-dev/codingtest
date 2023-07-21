n = int(input())
a = list(map(int, input().split()))
d = {}
for i in a:
    d[i] = 1
m = int(input())
b = list(map(int, input().split()))
for i in b:
    if d.get(i):
        if d[i] > 0:
            print(1, end=' ')
    else:
        print(0, end=' ')
