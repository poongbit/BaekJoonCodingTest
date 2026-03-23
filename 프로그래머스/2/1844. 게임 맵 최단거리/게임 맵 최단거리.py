from collections import deque

def solution(maps):
    answer = 0
    
    # 방문 도장 생성하기
    # 맵 바깥으로 나가면 안되므로 가로 세로 길이 저장
    n,m = len(maps), len(maps[0])
    
    visited = [[0] * m for _ in range(n)]
    
    # 칸의 개수의 최솟값 = 최단거리
    # BFS를 이용하기
    
    
    # 1을 0으로 바꿔서 방문 체크
    q = deque()
    
    q.append((0,0,1))
    
    while q:
        now_x,now_y,distance = q.popleft()
        
        # 상,하,좌,우
        dx = [0,0,-1,1]
        dy = [-1,1,0,0]
        
        for i in range(4):
            new_x = now_x + dx[i]
            new_y = now_y + dy[i]
            
            if (0<=new_x<m and 0 <=new_y < n):
                if maps[new_y][new_x] == 1:
                    if new_x == m-1 and new_y == n-1:
                        return distance + 1
                    
                    # 이제 지나간 길
                    maps[new_y][new_x] = 0
                    q.append((new_x,new_y,distance +1))
            
    return -1
                

