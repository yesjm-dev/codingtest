n = int(input())
stack = []
for _ in range(n):
    tc = int(input())
    if tc == 0:
        stack.pop()
    else:
        stack.append(tc)
result = 0
for i in stack:
    result+=i
print(result)