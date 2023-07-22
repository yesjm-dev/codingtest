n,m = map(int, input().split())
s = {}
count = 0
for _ in range(n):
    s[str(input())] = 1
for _ in range(m):
    tc = str(input())
    if s.get(tc):
        count+=1
print(count)