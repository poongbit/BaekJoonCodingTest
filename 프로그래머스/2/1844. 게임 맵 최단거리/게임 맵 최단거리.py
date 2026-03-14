from collections import deque


def solution(maps):
    
    answer = 0
    
    # 방문 도장 생성하기
    n,m = len(maps), len(maps[0])
    
    visited = [[0] * m for _ in range(n)]
    
    # 1,1은 방문했으므로 표기함
    visited[0][0] = 1
    
    # 큐 스택 초기화
    q = deque()
    
    # 좌표(x,y), 거리 초기화
    q.append((0,0,1))
    
    # 상,하,좌,우
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    
    # maps[행][열]
    
    while q:
        now_x, now_y , move = q.popleft()
        
        if now_x == m-1 and now_y == n-1:
            return move
        
        for i in range(4):
            x = now_x + dx[i]
            y = now_y + dy[i]
            
            if 0<=x<m and 0<=y<n and maps[y][x] == 1 and not visited[y][x]:
                visited[y][x] = True
                q.append((x,y,move+1))
    
    
    return -1


    

    
