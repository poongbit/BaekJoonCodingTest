import sys
input = sys.stdin.readline
from collections import deque


N,M = map(int,input().split())

graph = []

for _ in range(M):
    line = list(map(int,input().split()))
    graph.append(line)

visited = [[False]*(N) for _ in range(M)]


# 1인 토마토 찾기
find_tomato = []

for row in range(M):
    for column in range(N):
        if graph[row][column] == 1:
            find_tomato.append((row,column))



def BFS():
    # row,col,day
    q = deque([(r,c,0) for r,c in find_tomato])

    # 상,하,좌,우
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    day =0 

    while q:
        row, column,day = q.popleft()
        # 1 맨 끝은 방문 함
        visited[row][column] = True

        for i in range(4):
            new_row = row + dy[i]
            new_column = column + dx[i]

            if 0<=new_row<M and 0<=new_column<N:
                if graph[new_row][new_column] == -1:
                    pass
                elif graph[new_row][new_column] == 0:
                    if not visited[new_row][new_column]:
                        graph[new_row][new_column] = 1
                        q.append((new_row,new_column,day+1))

    return day

result = BFS()


for row in range(M):
    for column in range(N):
        if graph[row][column] == 0:
            print(-1)
            sys.exit()


print(result)



    