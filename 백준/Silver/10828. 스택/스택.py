import sys
input = sys.stdin.readline
n = int(input())
stack = []
for _ in range(n):
    word = input().split()
    order = word[0]
    if order == 'push':
        stack.append(int(word[1]))
    elif order == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif order == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    elif order == 'size':
        print(len(stack))
    elif order == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
