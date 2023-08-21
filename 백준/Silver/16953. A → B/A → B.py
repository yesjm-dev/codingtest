from collections import deque

a, b = map(int, input().split())
queue = deque([(a, 1)])
while queue:
    i, count = queue.popleft()
    if i == b:
        print(count)
        break
    if i * 2 <= b:
        queue.append((i * 2, count + 1))
    if i * 10 + 1 <= b:
        queue.append((i * 10 + 1, count + 1))
else:
    print(-1)
