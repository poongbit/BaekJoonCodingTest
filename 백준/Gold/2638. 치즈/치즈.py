import sys
input = sys.stdin.readline
from collections import deque

N,M = map(int,input().split())

graph = []

for _ in range(N):
    line = list(map(int,input().split()))
    graph.append(line)


"""
1. (0,0)에서 BFS → 외부 공기 전부 표시
2. 모든 치즈(1) 순회
   → 상하좌우 중 외부 공기에 2면 이상 닿으면 녹임
3. 치즈 다 녹을 때까지 반복
4. 시간(몇 시간 걸렸는지) 출력
"""

# 1. BFS에서 외부 공기 표시

def BFS_outside_air(x,y):

    # 출발 지점
    q = deque([(x,y)])

    # 상,하,좌,우
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    while q:
        now_x, now_y = q.popleft()

        for i in range(4):
            new_x = now_x + dx[i]
            new_y = now_y + dy[i]

            if 0<=new_x<M and 0<=new_y<N:

                if graph[new_y][new_x] == 0:
                    
                    # 바깥 공기 마주했다는 표시
                    graph[new_y][new_x] = 2
                    q.append((new_x,new_y))



# 실제로 치즈가 남아있는 지 확인
def has_cheese():
    for row in range(N):
        for column in range(M):
            if graph[row][column] == 1:
                return True
            
    return False


time = 0

while has_cheese():
    # 외부 공기 재표시
    for row in range(N):
        for column in range(M):
            if graph[row][column] ==2:
                graph[row][column] = 0


    # 외부 공기 재계산

    # 방문 공기 체크 추가
    graph[0][0] = 2
    BFS_outside_air(0,0)

    # 녹일 수 있는 치즈 찾기    
    to_melt = []
    
    for row in range(N):
        for column in range(M):
            if graph[row][column] == 1:
                
                outside_count = 0
                

                # 상,하,좌,우
                dx = [0,0,-1,1]
                dy = [-1,1,0,0]

                for i in range(4):
                    new_row = row + dy[i]
                    new_column = column + dx[i]

                    if 0<=new_row<N and 0<=new_column<M:
                        if graph[new_row][new_column] == 2:
                            outside_count +=1
                    
                if outside_count >=2:
                    to_melt.append((row,column))



    # 한꺼번에 녹이기

    for row,column in to_melt:
        graph[row][column] = 0

    time +=1

                        
print(time)