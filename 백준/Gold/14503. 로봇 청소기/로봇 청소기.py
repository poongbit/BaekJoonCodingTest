import sys
input = sys.stdin.readline

N,M = map(int,input().split())

# 로봇의 처음 위치
r,c,d = map(int,input().split())

# 방향 - 북 동 남 서
direction = [0,1,2,3]

graph = []

for _ in range(N):
    line = list(map(int,input().split()))
    graph.append(line)


# 로봇 청소기 작동 방식
# 0 : 청소 안됨, 1 : 벽

is_cleaned= 0

while True:
    # 현재 칸이 아직 청소가 되지 않은 경우, 현재 칸 청소
    # 청소 됨을 2로 표현하기

    if graph[r][c] == 0:
        graph[r][c] = 2
        is_cleaned +=1

    # 북,동,남,서 탐색
    dx = [0,1,0,-1]
    dy = [-1,0,1,0]

    # 4방향 탐색
    turned = False

    for _ in range(4):
        # 왼쪽으로 90도씩 돌려서 탐색 
        d = (d+3) % 4

        new_r = r + dy[d]
        new_c = c + dx[d]

        if 0<=new_r<N and 0<=new_c<M:
            if graph[new_r][new_c] == 0:
                # 앞으로 이동
                r,c = new_r,new_c
                turned = True
                break

    
    if not turned:
        # 바라보는 방향은 그대로 후진 가능
        # 북 동 남 서, 0,1,2,3
        back = (d+2) % 4

        check_r = r + dy[back]
        check_c = c + dx[back]

        if (0<=check_r<N and 0<=check_c<M) and graph[check_r][check_c] != 1:
            # 한칸 후진 가능
            r,c = check_r,check_c

        else:
            # 종료
            break


print(is_cleaned)

