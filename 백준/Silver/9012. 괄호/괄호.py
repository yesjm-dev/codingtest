n = int(input())
stack = []
for _ in range(n):
    ps = str(input())
    vps = True
    for i in ps:
        if i == '(':
            stack.append(i)
        else:
            if len(stack) > 0:
                stack.pop()
            else:
                vps = False
                break
    if len(stack) != 0 or vps == False:
        print('NO')
        stack.clear()
    else:
        print('YES')
