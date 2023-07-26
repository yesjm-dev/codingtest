from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
queue = deque()
for _ in range(n):
    tc = list(map(lambda s: s.strip(), input().split(' ')))
    if tc[0] == 'push':
        queue.append(tc[1])
    elif tc[0] == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif tc[0] == 'size':
        print(len(queue))
    elif tc[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif tc[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif tc[0] == 'back':
        if queue:
            l = len(queue)-1
            print(queue[l])
        else:
            print(-1)