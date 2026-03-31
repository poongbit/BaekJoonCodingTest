import sys
input = sys.stdin.readline
from collections import deque

N = int(input().strip())

graph = []

# 그래프 입력받기

for i in range(N):
    line = list(map(str,input().strip()))

    graph.append(line)

"""
1. 모든 곳을 순회하면서 탐험함
2. 방문 안한 칸을 발견 -> BFS로 탐색해서, 이어저 있는 곳
끝까지 연결함
3. BFS 끝날 때 마다 count +1
4. 적록색약은 R과 G가 같은 색으로 취급하고 다시 카운트

"""


# 방문 노드 설정하기

visited = [[False]*N for _ in range(N)]


def BFS(y,x,color,is_blind):
    
    # 초기 위치 설정
    q = deque([(y,x)])

    # 상,하,좌,우 탐색
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    while q:
        now_y,now_x = q.popleft()

        # 4방향 탐색
        for i in range(4):

            new_y = now_y + dy[i]
            new_x = now_x + dx[i]

            if 0<=new_y<N and 0<=new_x<N:
                # 조건을 만족하는 지
                if is_same_color(new_y,new_x,color,is_blind) and not visited[new_y][new_x]:
                    
                    # 방문 완료
                    visited[new_y][new_x] = True
                    q.append((new_y,new_x))



def is_same_color(y,x,color,is_blind):

    # is_blind가 True인 경우

    if is_blind:
        if color in ['G','R']:
            return graph[y][x] in ['G','R']
        
        else:
            return graph[y][x] == color
        
    else:
        return graph[y][x] == color


            
# 적록 색약이 아닌 사람과 맞는 사람을 탐색


count = 0

for y in range(N):
    for x in range(N):
        if not visited[y][x]:
            BFS(y,x,graph[y][x],False)
            count +=1

# 새 방문으로 판 갈기
visited = [[False]*N for _ in range(N)]

blind_count = 0

for y in range(N):
    for x in range(N):
        if not visited[y][x]:
            BFS(y,x,graph[y][x],True)
            blind_count +=1


print(count,blind_count)
