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

# 1. 빈 칸(0) 목록 수집
blank = [(i,j) for i in range(9) for j in range(9) if graph[i][j] == 0]

# 첫번 째 빈 칸에 1~9 시도

def check_num(y,x,num):

    # 행에 중복 있는 지 체크
    if num in graph[y]:
        return False
    

    # 열에 중복 있는 지 체크
    for i in range(9):
        if graph[i][x] == num:
            return False
        

    # 3 x 3 박스에 중복 있는 지 확인
    # 박스의 왼쪽 위가 시작점
    box_y =  (y //3) * 3
    box_x =  (x //3) * 3

    
    for y in range(box_y,box_y + 3):
        for x in range(box_x, box_x +3):
            if graph[y][x] == num:
                return False
    
    # 모든 걸 다 검증된 후 True 반환
    return True




def DFS(index):

    if index == len(blank):
        for row in graph:
            print(*row)

        sys.exit()

    # 빈칸에 채우기 위한 y,x 불러오기

    y,x = blank[index]

    # 1~9 숫자 작성하기
    for num in range(1,10):
        if check_num(y,x,num):
            graph[y][x] = num
            DFS(index+1)
            # 다시 백트래킹
            graph[y][x] = 0



DFS(0)
