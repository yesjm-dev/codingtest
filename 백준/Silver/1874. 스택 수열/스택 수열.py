# 복습 필요
n = int(input())
num = 1
stack = []
result = []
flag = True
for _ in range(n):
    now = int(input())
    while now >= num: 
        stack.append(num) # 입력한 수를 만날때까지 오름차순으로 push
        result.append('+')
        num += 1
        # 입력한 수를 만나면 while문 탈출

    if stack[-1] == now: # 스택 맨 위 숫자와 now가 동일하면 제거
        stack.pop()
        result.append('-')
    else: # 스택 수열을 만들 수 없음
        flag = False
        break

if flag:
    for i in result:
        print(i)
else:
    print('NO')
