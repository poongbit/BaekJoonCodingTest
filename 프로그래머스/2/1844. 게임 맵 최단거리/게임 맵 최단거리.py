from collections import deque

def BFS(x,y,visited,maps,n,m):
    q = deque()
    
    visited[x][y] = True
    
    q.append((x,y,1)) # 시작점, 거리 1
    
    # 이동 좌표 (상,하,좌,우)
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    
    while q:
        now_x, now_y, move = q.popleft()
        
        if now_x == n-1 and now_y == m-1:
            return move
        
        for i in range(4):
            x = now_x + dx[i]
            y = now_y + dy[i]
            
            if 0<=x<n and 0<=y<m and maps[x][y] !=0 and not visited[x][y]:
                visited[x][y] = True
                q.append((x,y,move+1))
                
        
    return -1
            
            

def solution(maps):
    answer = 0
    
    # 1. 입력값 받기 및 변수 선언
    
    n = len(maps)
    
    m = len(maps[0])
    
    visited = [[False] * (m) for i in range(n)]
    
    answer = BFS(0,0,visited,maps,n,m)
        
    
    
    return answer