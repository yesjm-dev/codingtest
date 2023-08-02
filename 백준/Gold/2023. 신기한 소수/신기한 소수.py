# 소수인지 판별
def isPrime(y):
    for i in range(2, int(y**0.5) + 1):
        if y % i == 0:
            return False
    return True

def dfs(x, j):
    if j == n: # n과 자릿수가 동일할때
        if isPrime(x): # 소수이면 출력
            print(x)
        return
    for i in range(1, 10): # 1~9 반복하면서
        if i % 2 == 0: # 짝수는 제외하고
            continue
        if isPrime(x * 10 + i): # x*10+i가 소수이면
            dfs(x * 10 + i, j + 1) # 자리수 늘려서 재귀 호출

n = int(input())
dfs(2, 1)
dfs(3, 1)
dfs(5, 1)
dfs(7, 1)
