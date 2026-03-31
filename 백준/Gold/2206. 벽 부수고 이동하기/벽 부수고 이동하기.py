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
    # 상,하,좌,우
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    # 이동거리
    
    # 벽 한번 부섰는 지 여부
    break_walls = False
    q = deque([(0,0,1,break_walls)])

    visited = [[[False]*2 for _ in range(M)] for _ in range(N)]

    visited[0][0][0] = True
    

    while q:
        now_x,now_y,d,is_broken = q.popleft()

        if now_x == M-1 and now_y == N-1:
            return d

        
        # 4방향 탐색

        for i in range(4):
            new_x = now_x + dx[i]
            new_y = now_y + dy[i]

            # map 안에 위치해 있고
            if 0<=new_x<M and 0<=new_y<N:
                # 만약에 도착했으면 종료
                
                # 0이 존재하면 갈 수 있음
                if graph[new_y][new_x] == 0 and not visited[new_y][new_x][is_broken]:
                    visited[new_y][new_x][is_broken] = True
                    q.append((new_x,new_y,d+1,is_broken))

                # 벽이 있어도 한번은 부술 수 있음

                elif graph[new_y][new_x] == 1 and not is_broken and not visited[new_y][new_x][1]:
                    visited[new_y][new_x][1] = True
                    q.append((new_x,new_y,d+1,True))

    return -1


result = BFS()

print(result)



            


