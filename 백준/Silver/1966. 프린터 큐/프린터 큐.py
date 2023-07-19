from collections import deque

tc = int(input())
for _ in range(tc):
    N, M = map(int, input().split())
    deq = deque(list(map(int, input().split())))
    count = 0
    while 1:
        best = max(deq)
        first = deq.popleft()
        M -= 1
        if best == first:
            count += 1
            if M < 0:
                print(count)
                break
        else:
            deq.append(first)
            if M < 0:
                M = len(deq)-1