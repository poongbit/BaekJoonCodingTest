import sys
input = sys.stdin.readline

graph = []

# 1. 그래프 입력받기
for _ in range(9):
    line = list(map(int,input().split()))
    graph.append(line)



"""
1. DFS 로 탐색해보기
2. DFS를 이용해 어디에 숫자를 집어 넣어야 하는가?
3. 빈칸을 채워넣어야 하는데, 목록을 미리 뽑아두면, index로
관리 가능!

"""

blanks = [(i,j) for i in range(9) for j in range(9) if graph[i][j] == 0]

def is_valid(row,column,num):

    # 열을 순회하면서 체크   
    for i in range(9):
        # 이미 같은 숫자가 있다면, False 반환
        if graph[row][i] == num:
            return False
        
    # 행을 순회하면서 체크

    for j in range(9):
        # 이미 같은 숫자가 있다면, False 반환
        if graph[j][column] == num:
            return False
        
    
    # 3*3 을 체크, 시작점을 구하기

    box_row = (row // 3) * 3
    box_column = (column // 3) * 3

    for row in range(box_row,box_row +3):
        for column in range(box_column, box_column + 3):
            if graph[row][column] == num:
                return False
            
    # 다 체크 완료가 됐으면, True 반환

    return True


def DFS(index):
    # 종료 조건
    if index == len(blanks):
        for row in graph:
            print(*row)
        sys.exit()

    # 0이 있는 row,column을 반환
    row,column = blanks[index]
    
    # 1~9까지 숫자를 집어 넣어보기
    for num in range(1,10):

        if is_valid(row,column,num):
            # 조건을 만족하므로 숫자를 집어넣음
            graph[row][column] = num
            # 그 다음 탐색으로 넘어감
            DFS(index+1)
            # 잘 안됐을 때, 다시 도로 돌려넣음
            graph[row][column] = 0


DFS(0)