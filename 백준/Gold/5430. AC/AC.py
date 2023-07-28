import sys
input = sys.stdin.readline
from collections import deque

t = int(input())
for _ in range(t):
    p = list(input().strip())
    n = int(input().strip())
    queue = deque(map(str, input().strip()[1:-1].replace(',', ' ').split()))
    flag = 0
    for i in p:
        if i == 'R':
            flag += 1
        else:
            if queue:
                if flag % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()
            else:
                print('error')
                break
    else:
        if flag % 2 == 0:
            print("[" + ",".join(queue) + "]")
        else:
            queue.reverse()
            print("[" + ",".join(queue) + "]")