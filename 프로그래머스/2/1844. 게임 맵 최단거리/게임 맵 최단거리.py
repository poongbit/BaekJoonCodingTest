from collections import deque

            
def solution(maps):
    
    # 입력값 받기 
    n,m = len(maps),len(maps[0])
    
    # 방문 도장 만들기
    visited = [[False] * m for _ in range(n)]
    
    # 현재 (1,1) 방문한 상태임
    visited[0][0] = True
    
    # 큐에 거리 같이 들고 다님
    # 튜플을 받으려면 통째로 []로 감싸야 함
    q = deque([(0,0,1)])
    
    # 상,하,좌,우
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    
    while q:
        now_x, now_y,move = q.popleft()
        
        if now_x == n-1 and now_y == m-1:
            return move
        
        for i in range(4):
            x = now_x + dx[i]
            y = now_y + dy[i]
            
            if 0<=x<n and 0<=y<m and maps[x][y] != 0 and not visited[x][y]:
                visited[x][y] = True
                q.append((x,y,move+1))
    
    return -1
    
