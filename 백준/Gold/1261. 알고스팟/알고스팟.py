import sys
from collections import deque

input = sys.stdin.readline

N,M = map(int,input().split())

graph = []

for _ in range(M):
    line = list(map(int,input().strip()))
    graph.append(line)

# 2. 탐색하기

visited = [[False]*N for _ in range(M)]


def BFS():
    
    # 초기 시작점
    # x,y, 벽을 부순 횟수
    q = deque([(0,0,0)])

    # 위치 방문함
    visited[0][0] = True

    # 상,하,좌,우
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]



    while q:
        x,y,cost = q.popleft()

        if x == N-1 and y == M-1:
            return cost
        
        # 상,하,좌,우 탐색

        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]

            if 0<=new_x<N and 0<=new_y<M:

                # 그 위치가 빈 방이라면 이동
                if graph[new_y][new_x] == 0 and not visited[new_y][new_x]:
                    
                    visited[new_y][new_x] = True

                    q.appendleft((new_x,new_y,cost))


                # 벽을 마주할 때, 부수거나, 그냥 회피하거나?

                elif graph[new_y][new_x] == 1 and not visited[new_y][new_x]:

                    visited[new_y][new_x] = True

                    q.append((new_x,new_y,cost+1))


result = BFS()

print(result)
