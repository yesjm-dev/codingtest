# set의 교집합 이용
n,m = map(int, input().split())
a = set()
b = set()
for _ in range(n):
    a.add(str(input()))
for _ in range(m):
    b.add(str(input()))

# 교차하는 이름들을 찾는다
result = sorted(list(a & b))

print(len(result))
for i in result:
    print(i)
