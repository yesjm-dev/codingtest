n = int(input())
time = []
count = 0
last = 0
for _ in range(n):
    a, b = map(int, input().split())
    time.append([a, b])
time = sorted(time, key=lambda a: a[0]) # 시작 시간 기준 오름차순
time = sorted(time, key=lambda a: a[1]) # 끝나는 시간 기준 오름차순

for i, j in time:
    if i >= last: 
        count += 1
        last = j
print(count)