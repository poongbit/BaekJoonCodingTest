import sys
input = sys.stdin.readline

graph = []

# 1. 그래프 입력받기
for _ in range(9):
    line = list(map(int,input().split()))
    graph.append(line)

"""
**올바른 접근 — 백트래킹**
```
1. 빈 칸(0) 목록 수집
2. 첫 번째 빈 칸에 1~9 시도
3. 행/열/3x3 박스에 중복 없으면 다음 빈 칸으로
4. 막히면 되돌아오기
"""

blank = [(i,j) for i in range(9) for j in range(9) if graph[i][j]==0]


# 3번을 검증하기 위한 함수를 만들기
# 같은 수가 중복으로 있으면 어차피 안됨
def check_num(y,x,num):

    # 행 검사
    if num in graph[y]:
        return False
    

    # 열 체크
    for i in range(9):
        if graph[i][x] == num:
            return False
        

    # 3 x 3 체크
    box_y = (y//3) * 3
    box_x = (x//3) * 3

    for y in range(box_y,box_y+3):
        for x in range(box_x,box_x+3):
            if graph[y][x] == num:
                return False
            
    # 위 3가지를 다 검증했다면, true
    return True



def DFS(index):
    # 인덱스가 blank를 다 채우면
    if index == len(blank):
        for row in graph:
            print(*row)

        sys.exit()

    # blank에서 비어있는 공간 꺼내기
    y,x = blank[index]

    # 숫자를 하나씩 집어넣음
    for num in range(1,10):
        if check_num(y,x,num):
            graph[y][x] = num
            DFS(index+1)
            # 백트래킹으로 다시 복구
            graph[y][x] = 0

  
DFS(0)

