# https://resilient-923.tistory.com/164 참고함. 복습 필요
n, m = map(int, input().split())
r, c, d = map(int, input().split())
matrics = []
visited = [[0] * m for _ in range(n)]

# 방향 설정용(왼쪽, 아래, 오른쪽, 위쪽 탐색해야함)
dx = [-1,0,1,0]
dy = [0,1,0,-1]

for _ in range(n):
    matrics.append(list(map(int, input().split())))

# 처음 시작하는 곳 방문 처리
visited[r][c] = 1
count = 1

while True:
    flag = 0
    # 4방향 확인
    for _ in range(4):
        # 0, 3, 2, 1 순서를 만들기 위한 식
        nx = r + dx[(d+3)%4]
        ny = c + dy[(d+3)%4]
        # 한번 돌았으면 그 방향으로 작업 시작
        d = (d+3)%4
        if 0 <= nx < n and 0 <= ny < m and matrics[nx][ny] == 0:
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                count += 1
                r = nx
                c = ny
                # 청소를 한 방향이라도 했으면 다음으로 넘어감
                flag = 1
                break
    # 4방향 모두 청소가 되어있을때
    if flag == 0: 
        # 후진했는데 벽인 경우
        if matrics[r-dx[d]][c-dy[d]] == 1: 
            print(count)
            break
        else:
            r = r-dx[d]
            c = c-dy[d]
