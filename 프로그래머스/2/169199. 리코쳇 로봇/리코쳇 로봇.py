# 간단한 아침 문제입니다. 
# 2차코테 2번정도의 난이도로 30분 안에 풀 수 있어야 합니다.
from collections import deque

def solution(board):
    
    """
    1) R,G 파악하기 - R : 로봇의 처음 위치, D - 장애물 위치, G - 목표 지점
    2) 슬라이딩 하는 움직임 함수 구현
    3) BFS를 통해 최소 거리 구하기
    
    
    """
    answer = 0
    
    # 세로, 가로
    N = len(board)
    M = len(board[0])
    
    # R 위치 확인하기 
    
    for row in range(N):
        for column in range(M):
            if board[row][column] == 'R':
                R_row, R_column = row,column
                break
                
    # G 위치 확인하기
    
    for row in range(N):
        for column in range(M):
            if board[row][column] == 'G':
                G_row, G_column = row,column
                break
    
    # 상,하,좌,우 이동
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    
    
    # 슬라이딩하는 함수 구하기
    def slide(row,column,dx,dy):
        # for 구문으로 반복하긴 어려우므로 while
        # 벽이나 D에 부딫히기 전까지는 움직임
        
        while (0<=row +dy <N and 0<=column+dx <M) and (
        board[row+dy][column+dx] != 'D'):
            
            # 같은 방향으로 쭉 이동
            row += dy
            column += dx

        return row,column
    
    # 방문 노드 생성
    visited = [[False] * M for _ in range(N)]
    
    def BFS():
        # 초기 지점 , R의 row/column, 거리
        q = deque([(R_row,R_column,0)])
        
        # 방문 노드 방문 체크
        visited[R_row][R_column] = True
        
        # 상,하,좌,우 이동
        dx = [0,0,-1,1]
        dy = [-1,1,0,0]
        
        while q:
            n_row, n_column, move = q.popleft()
            
            if n_row == G_row and n_column == G_column:
                return move
            
            for i in range(4):
                u_row,u_col = slide(n_row,n_column,dx[i],dy[i])
                
                if not visited[u_row][u_col]:
                    visited[u_row][u_col] = True
                    q.append((u_row,u_col,move + 1))
            
                    
        # 없으면 -1 반환   
        return -1
    
    
    answer = BFS()
    
    
    return answer