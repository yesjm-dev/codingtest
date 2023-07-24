while True:
    stack = []
    tc = str(input())
    if tc == '.':
        break
    for i in tc:
        if i == '(' or i == '[':
            stack.append(i)
        elif i ==')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
                break
        elif i ==']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(i)
                break
    if len(stack) == 0:
        print('yes')
    else:
        print('no')