from collections import Counter

n = int(input())
card = list(map(int, input().split()))
m = int(input())
M = list(map(int, input().split()))

count = Counter(card)
for i in range(m):
    if M[i] in count:
        print(count[M[i]], end=' ')
    else:
        print(0, end=' ')