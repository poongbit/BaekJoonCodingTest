from collections import deque

def solution(maps):
    
    answer = 0
    
    # n과 m의 개수 구하기 
    n,m = len(maps), len(maps[0])
    
    # 방문 도장 생성하기
    # maps가 0-based index이므로 굳이 +1 안함
    visited = [[False] * m for _ in range(n)]
    
    #(1,1) 위치에 있으므로 visited는 이미 방문
    visited[0][0] = True
    
    # 따로 DFS,BFS 함수 만들면 매개변수로 많이 만들어야 하므로, 귀춘
    
    # 시작점,거리를 추가
    # 거리는 나중에 칸의 개수의 최솟값을 맞추기 위해 추가함
    q = deque([(0,0,1)])
    
    # 상,하,좌,우 이동
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    
    while q:
        now_x, now_y, move = q.popleft()
        
        # 베이스 조건 : 끝자락에 도착한 경우
        if now_x == n-1 and now_y == m-1:
            return move
        
        # 4방향 전부 이동하면서 체크
        
        for i in range(4):
            x = now_x + dx[i]
            y = now_y + dy[i]
            
            if 0<=x<n and 0<=y<m and maps[x][y] != 0 and not visited[x][y]:
                # 방문 도장 찍기
                visited[x][y] = True
                # 다음 확장으로 넘어가기
                q.append((x,y,move+1))
        
    # 큐 스택이 다 돌아도 해결 못한 경우
    return -1
    

    
