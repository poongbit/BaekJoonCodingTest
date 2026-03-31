import sys
input = sys.stdin.readline
from collections import deque

N,M = map(int,input().split())

graph = []

for i in range(N):
    line = list(map(int,input().strip()))
    graph.append(line)


# 최단거리 구하기 - deque
"""
0 : 이동할 수 있는 곳
1 : 이동할 수 없는 벽

"""

def BFS():

    # 무환 회귀를 막기 위한 방문 도장 생성
    visited = [[[False] * 2 for _ in range(M)] for _ in range(N)]

    # 초기 노드는 방문
    # 방문을 부순 경우와 아닌 경우를 ([False],[False]) 로 구분
    visited[0][0][0] = True

    # 벽을 한번 부수고 갈 수 있음
    is_broken = False

    # 초기 x,y 좌표, 거리
    q = deque([(0,0,1,is_broken)])

    # 상,하,좌,우
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    while q:
        now_x,now_y,distance, is_broken = q.popleft()

        # 종료 조건을 앞에 두기
        if now_x == M-1 and now_y == N-1:
            return distance 

        # 4방향 탐색

        for i in range(4):
            x = now_x + dx[i]
            y = now_y + dy[i]

            if 0<=x<M and 0<=y<N:
                # 만약 0이 있다면 그곳으로 이동
                if graph[y][x] == 0 and not visited[y][x][is_broken]:
                    visited[y][x][is_broken] = True
                    q.append((x,y,distance+1,is_broken))

                # 1이 있지만, is_broken이 False인 경우

                elif graph[y][x] == 1 and not is_broken and not visited[y][x][is_broken]:
                    visited[y][x][is_broken] = True
                    q.append((x,y,distance+1,True))

    return -1

result = BFS()

print(result)