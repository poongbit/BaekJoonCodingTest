import sys
input = sys.stdin.readline
from collections import deque

N,M = map(int,input().split())

graph = []

for _ in range(N):
    line = list(map(int,input().split()))
    graph.append(line)


"""
1. 외부 공기 계산

2. 녹여야할 치즈가 있는 동안:
    외부 공기 계산
    외부 공기 노출이 2번 이상 있으면 녹임


"""

def BFS():
    q = deque([(0,0)])

    # 외부 공기를 2로 체크함
    graph[0][0] = 2

    # 상,하,좌,우
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    while q:
        row,column = q.popleft()

        for i in range(4):
            new_row = row + dy[i]
            new_column = column + dx[i]

            if 0<=new_row<N and 0<=new_column<M:
                if graph[new_row][new_column] == 0:
                    graph[new_row][new_column] = 2
                    q.append((new_row,new_column))

                    

# 치즈가 아예 사라질 때까지 반복해야 함

def has_cheese():
    
    for row in range(N):
        for column in range(M):
            if graph[row][column] == 1:
                return True

    return False


time = 0
while has_cheese():

    # 1. BFS로 외부 공기 체크하기

    BFS()

    # 2. 외부 공기가 2 이상 닿은 곳을 체크하기

    # 상,하,좌,우
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    # 녹여야 할 치즈 계산
    cheese_left = []

    for row in range(N):
        for column in range(M):
            if graph[row][column] == 1:
                count = 0
                # 치즈가 있는 곳에서 외부 공기가 2 이상이면

                for i in range(4):
                    new_row = row + dy[i]
                    new_column = column + dx[i]

                    if 0<=new_row<N and 0<=new_column<M:
                        if graph[new_row][new_column] == 2:
                            count +=1

                
                if count >=2:
                    cheese_left.append((row,column))

    # 치즈를 녹여야할 위치를 꺼내 0으로 바꿈

    for row,column in cheese_left:
        graph[row][column] = 0

    
    #치즈를 녹인 후 시간 1초가 지남
    time +=1

    # 남아있는 외부 공기 2는 다시 0으로 바꿔줘서
    # 다시 외부 공기 계산할 수 있도록 변경

    for row in range(N):
        for column in range(M):
            if graph[row][column] == 2:
                graph[row][column] = 0



print(time)