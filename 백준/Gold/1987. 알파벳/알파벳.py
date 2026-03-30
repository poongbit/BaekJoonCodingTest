import sys
input = sys.stdin.readline
from collections import deque

R,C = map(int,input().split())


graph = [[0]*C for _ in range(R)]

for i in range(R):
    line = list(str(input().strip()))

    for j in range(len(line)):
        graph[i][j] = line[j]



# 방문 노드 기록
# 상 하 좌 우 이동

dx = [0,0,-1,1]
dy = [-1,1,0,0]

#최대, 최소 = BFS 사용

# 초기 - 왼쪽 위 

def DFS(y,x,visited):
    ans = len(visited)

    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]

        if 0<=new_x<C and 0<=new_y<R:
            letter = graph[new_y][new_x]
            if letter not in visited:
                visited.add(letter)
                ans = max(ans,DFS(new_y,new_x,visited))
                visited.remove(letter) # 백트래킹


    return ans

visited = {graph[0][0]}

print(DFS(0,0,visited))