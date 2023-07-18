t = int(input())
for _ in range(t):
    stack = []
    ps = str(input())
    for i in ps:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack:
                stack.pop()
            else:
                print('NO')
                break
    else: # break문으로 끊기지 않고 수행됬을경우 수행한다
        if not stack:
            print('YES')
        else:
            print('NO')
