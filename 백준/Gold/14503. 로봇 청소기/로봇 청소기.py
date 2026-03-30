import sys
input = sys.stdin.readline

N,M = map(int,input().split())

# r,c,d 좌표
# 북,동,남,서
direction = [0,1,2,3]

y,x,d = map(int,input().split())


dx = [0,1,0,-1]
dy = [-1,0,1,0]



# 1. 그래프 입력 받기
graph = [[0] * M for _ in range(N)]

for i in range(N):
    line = list(map(int,input().split()))

    for j in range(len(line)):
        graph[i][j] = line[j]


# 2. 시뮬레이션 돌리기
# 0 : 청소 안됨, 1: 벽

# 청소한 횟수
cleaned = 0
while True:
    # 현재 칸이 청소가 되지 않은 경우, 청소한다.
    if graph[y][x] == 0:
        graph[y][x] = 2
        cleaned +=1

    # 4방향 탐색하기
    # 90 도 회전하면서 탐색, 반시계

    turned = False

    for i in range(4):
        # ex) d = 0, next_d = 3
        d = (d - 1) % 4

        new_x = x + dx[d]
        new_y = y + dy[d]

        if graph[new_y][new_x] == 0:
            turned = True
            # 한 칸 앞으로 전진
            x,y = new_x, new_y
            break

    # 한번도 회전을 안 했을 경우
    if not turned:
        # 후진하기
        back = (d+2) % 4
        current_x = x + dx[back]
        current_y = y + dy[back]

        if graph[current_y][current_x] == 1:
            break

        else:
            # 후진 한다
            x,y = current_x,current_y
    

print(cleaned)