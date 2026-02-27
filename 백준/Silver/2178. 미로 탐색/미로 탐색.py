# 문제 30 - 미로 탐색하기 2178번

"""
dx, dy (상하좌우를 탐색하기 위한 define값 정의 변수)
N(row), M(column)
A (데이터 저장 2차원 행렬)

visited (방문 기록 저장 리스트)

for N만큼 반복:
    for M만큼 반복:
        A 리스트에 데이터 저장


#BFS 구현하기

BFS:
    큐에 시작 노드 삽입
    visited 리스트에 현재 노드 방문 기록
    while 큐가 빌 때까지:
        큐에서 노드 데이터를 가져오기
        for 상하좌우 탐색:
            if 유효한 좌표:
                if 이동할 수 있는 칸이면서 방문하지 않은 노드:
                    visited 리스트에 방문 기록
                    A 리스트에 depth를 현재 노드의 depth + 1로 업데이트
                    큐에 데이터 삽입


BFS(0,0) 실행
A[N-1][M-1] 출력


"""

import sys
from collections import deque

# 1. 미로의 크기 N(층수, row), M(호수, column) 입력받기
N,M  = map(int,input().split())

# 2. 미로 지도 입력받기 (띄어쓰기 없이 붙어있는 숫자들은 리스트로 변환)
A = [list(map(int, input().strip())) for _ in range(N)]

# 3. 방문 기록 수첩 : (N * M 크기로 False 채우기)
visited = [[False] * M for _ in range(N)]

# 4. 상하좌우 나침반 (row와 column의 이동방향)
# 위, 아래, 왼쪽, 오른쪽

dr = [-1,1,0,0] # 층수(세로 이동) : 위로 1칸, 아래로 1칸, 그대로, 그대로
dc = [0,0,-1,1] # 호수(가로 이동) : 그대로, 그대로, 왼쪽 1칸, 오른쪽 1칸

def BFS(start_r,start_c):
    queue = deque()
    queue.append((start_r,start_c)) # 대기열에 시작 좌표 넣기
    visited[start_r][start_c] = True # 시작점 방문 도장 찍기

    # 대기열에 탐색할 좌표가 남아있는 동안 계속 반복
    while queue:
        # 1) 대기열에서 맨 앞사람 꺼내기
        now_r, now_c = queue.popleft()

        # 2) 현재 위치에서 상하좌우 4방향으로 찔러보기
        for i in range(4):
            next_r = now_r + dr[i]
            next_c = now_c + dc[i]

            # 3) 체크 1: 미로 밖으로 튀어나가지 않았는가? (유효한 좌표 체크)
            if 0 <= next_r < N and 0 <= next_c < M:
                
                # 4) 체크 2: 갈수 있는 길(1)이고, 아직 안 가본 곳(False)인가?

                if A[next_r][next_c] == 1 and not visited[next_r][next_c]:

                    visited[next_r][next_c] = True # 방문 도장 찍기


                    # 5) 다음 칸 바닥에 '현재 내 걸음수 + 1'을 적어두기

                    A[next_r][next_c] = A[now_r][now_c] + 1


                    # 6) 다음 칸을 대기열에 추가 (물결이 한 칸 더 퍼져나감)

                    queue.append((next_r,next_c))



# 시작점 (0,0)에서 물방울 떨어뜨리기
BFS(0,0)

# 도착점 바닥에 있는 최종 걸음 수 출력
print(A[N-1][M-1])
