import sys
input = sys.stdin.readline
sys.setrecursionlimit(500 * 500 + 100)
"""
한 칸 - 한 지점
각 칸마다 그 지점의 높이, 이동 - 상 하 좌 우 

세준 : 제일 왼쪽 위

맨 오른쪽 아래로 가는 걸 목표:
가능한 항상 높이가 더 낮은 지점으로만 이동

내리막길로만 이동하는 경로의 개수?

"""

M,N = map(int,input().split())

graph = []

for _ in range(M):
    number_list = list(map(int,input().split()))
    graph.append(number_list)


"""
dp[row][column] : row,column에 위치할 때, 내리막길로 이동한 경로의 개수


DFS 구성

DFS(x,y)좌표 구성
dp[y][x]가 방문하지 않은 곳이라면 방문 체크

인덱스를 담을 리스트 

4 방향 탐색:
    현재 위치보다 작은 높이를 가진 인덱스 기록

인덱스 안 리스트를 꺼내서:
    그 리스트가 방문되지 않았으면:
        dp[인덱스] += dp(그 이전 인덱스)
        DFS(새로운 x,y)


"""

dp = [[-1] * N for _ in range(M)]


def DFS(x,y):
    # 만약, 도착지에 도착했다면, 1을 반환
    if x == N-1 and y == M-1:
        dp[y][x] = 1
        return dp[y][x]
    
    # memorization 활용
    if dp[y][x] != -1:
        return dp[y][x]
    
    # 방문 했으므로, -1에서 0으로 전환 

    dp[y][x] = 0

    # 상,하,좌,우
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]

        if 0<=new_x<N and 0<=new_y<M:
            if graph[new_y][new_x] < graph[y][x]:
                dp[y][x] += DFS(new_x,new_y)

    return dp[y][x]

DFS(0,0)

print(DFS(0,0))