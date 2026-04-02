# 간단한 아침 문제입니다. 
# 2차코테 2번정도의 난이도로 30분 안에 풀 수 있어야 합니다.

from collections import deque

def solution(board):
    answer = 0
    
    # R 지점 찾기
    
    for row in range(len(board)):
        for column in range(len(board[0])):
            if board[row][column] == 'R':
                R_row, R_column = row,column
                break
    
    
    
    # G 지점 찾기
    
    for row in range(len(board)):
        for column in range(len(board[0])):
            if board[row][column] == 'G':
                G_row, G_column = row,column
                break
    
    
    
    # 한 방향으로 벽/장애물 만날 때 까지 쭉 이동:
    
    def slide(row,col,dr,dc):
        while (0<=row + dr <len(board) 
               and 0 <=col + dc <len(board[0])
              and board[row+dr][col+dc] != 'D'):
            
            row += dr
            col += dc
        
        return row,col
    
    
    
    def BFS():
        q = deque([(R_row,R_column,0)])
        
        # 상,하,좌,우
        dr = [0,0,-1,1]
        dc = [-1,1,0,0]
        
        
        # 방문 노드 생성
        visited = [[False] * len(board[0]) for _ in range(len(board))]
        visited[R_row][R_column] = True
        
        while q:
            # 현재 노드, 칼럼 위치 반환
            n_row, n_col,count = q.popleft()
            
            if n_row == G_row and n_col == G_column:
                return count
            
            
            # 슬라이딩 진행
            for i in range(4):
                new_row, new_col = slide(n_row,n_col,dr[i],dc[i])
                
                if not visited[new_row][new_col]:
                    visited[new_row][new_col] = True
                    q.append((new_row,new_col,count+1))
        
        # 다 만족하지 않으면 -1 반환
        return -1
                    
    
    answer = BFS()
    
    return answer
    