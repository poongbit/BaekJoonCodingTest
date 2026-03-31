import sys
input = sys.stdin.readline
from collections import deque

N = int(input().strip())

graph = []

# 그래프 입력받기

for i in range(N):
    line = list(map(str,input().strip()))

    graph.append(line)




# 방문 노드 만들기

visited = [[False] * N for _ in range(N)]

"""
1. 모든 곳을 순회하면서 탐험함
2. 방문 안한 칸을 발견 -> BFS로 탐색해서, 이어저 있는 곳
끝까지 연결함
3. BFS 끝날 때 마다 count +1
4. 적록색약은 R과 G가 같은 색으로 취급하고 다시 카운트

"""

def is_same_color(x,y,color,is_blind):
    # 만약에 적녹색약이면 R-G는 같은 색으로 구분

    if is_blind:
        
        if color in ['G','R']:
            return graph[y][x] in ['G','R']

        else:
            return graph[y][x] == color
        

    else:
        return graph[y][x] == color
    
    





def BFS(start_x,start_y,color,is_blind):
    q = deque([(start_x,start_y)])

    # 노드 방문 성공
    visited[start_y][start_x] = True

    # 상,하,좌,우
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    while q:
        now_x,now_y = q.popleft()

        # 4방향 죄표 탐색
        for i in range(4):
            x = now_x + dx[i]
            y = now_y + dy[i]

            if (0<=x<N and 0<=y<N) and not visited[y][x]:
                if is_same_color(x,y,color,is_blind):
                    # 방문 도장 쾅 찍기
                    visited[y][x] = True
                    q.append((x,y))


count = 0

for y in range(N):
    for x in range(N):
        if not visited[y][x]:
            BFS(x,y,graph[y][x],False)
            count +=1

# 카운트를 하기 위한 새 방문 노드작성
visited = [[False] * N for _ in range(N)]

# 적록 색약인 사람이 방문하는 것
blind_count = 0

for y in range(N):
    for x in range(N):
        if not visited[y][x]:
            BFS(x,y,graph[y][x],True)
            blind_count +=1


print(count,blind_count)

        