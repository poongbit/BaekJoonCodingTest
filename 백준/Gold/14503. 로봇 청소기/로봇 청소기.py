from collections import deque

import sys
input = sys.stdin.readline

N,M = map(int,input().split())

# 로봇 청소기가 있는 칸의 좌표

y,x,d = map(int,input().split())


# 북,동,남,서 일 떄, (x,y)의 변화량
face = [0,1,2,3]

dx = [0,1,0,-1]
dy = [-1,0,1,0]

graph = []

for _ in range(N):
    line = list(map(int,input().split()))
    graph.append(line)


"""
[[1, 1, 1], 
[1, 0, 1],
[1, 1, 1]]
"""

# 청소한 양
cleaned = 0

while True:
    
    # 지금 위치한 자리에 청소해야 하는 지
    if graph[y][x] == 0:
        graph[y][x] = 2 # 청소 표시
        cleaned +=1

    # 화전해야 하는 지 여부 체크
    turned = False

    # 왼쪽부터 4방향 탐색
    # 반시계 90도 회전이므로 -1씩 빠짐
    for i in range(4):
        d = (d - 1) % 4
        
        new_x = x + dx[d]
        new_y = y + dy[d]

        if graph[new_y][new_x] == 0: # 안 청소된 빈칸
            # 앞으로 한칸 전진
            x,y = new_x,new_y
            turned = True
            break

    # 청소되지 않은 빈칸이 없는 경우
    # 후진하기
    if not turned:
        back = (d + 2) % 4
        check_x = x + dx[back]
        check_y = y + dy[back]

        if graph[check_y][check_x] != 1:
            x,y = check_x,check_y

        else:
            break


print(cleaned)



