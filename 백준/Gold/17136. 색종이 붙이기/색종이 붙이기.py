# 문제 28 - 색종이 붙이기

"""
M :  종이 상태를 저장하는 배열
S : 남은 색종이 수 저장 배열
result : 최소로 사용한 개수 저장
r : row , c: column

10 * 10 크기의 종이 데이터를 입력받아 M에 저장하기
백트래킹 함수 실행 (시작 좌표 0, 사용한 색종이 수 0)

can_attatch (r,c, 크기):
    size * size 범위가 종이 크기를 넘지 않고
    모두 1인지 확인


fill(r, c, 크기, 채울 값):
    size * size 범위 내의 모든 칸을 value로 채우기 (0 또는 1)


# 백트래킹 상세 구현하기
backtrack(현재 위치, 사용한 색종이 수):
    if 모든 좌표를 탐색한 경우:
        현재까지 사용한 색종이 수로 최솟값 갱신
        함수 종료

    
    현재 위치의 좌표 (r,c)를 계산

    if 현재까지 사용한 색종이 수가 최솟값 이상이면:
        더 이상 탐색할 필요가 없으므로 종료 (가지치기)

    if 현재 위치가 1이라면:
        크기 5부터 1까지 색종이 크기 순서대로 시도하면서:
            if 해당 크기 색종이가 남아 있고, 해당 위치에 색종이를 붙힐 수 있다면:
                색종이 사용 처리
                종이의 해당 영역을 0으로 덮음
                다음 위치로 이동하여 재귀 탐색 수행

    else (현재 위치가 0이라면):
        다음 위치로 이동하여 그대로 탐색 진행

if result가 초깃값 그대로라면:
    -1 출력

else:
    최초로 사용한 색종이 개수 출력


"""


import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 종이 데이터 입력 받기
M = [list(map(int,input().split())) for _ in range(10)] #[[],[],[],[],[],[],....[]] / 입력 받은 숫자 배열이 10개

# 색종이 수 (크기가 1 ~ 5까지 각각 최대 5장)
S = [0,5,5,5,5,5] # 더미 데이터 index 0

result = float('inf') # infinity, 나중에 result를 보여줄 수 있는 지 조건 표시를 해줌


"""
비유: 아파트

row : (행,줄) - 몇 층인가요?, row가 바뀌는 건 위 아래가 움직이므로 세로(y좌표)를 결정함
column: (열,칸) - 몇 호인가요?, colum이 바뀌는 건 왼쪽 오른쪽이 바뀌므로 가로(x좌표)를 결정



"""
def fill(row, column, size, value):
    for i in range(row, row + size):
        for j in range(column, column + size):
            M[i][j] = value


def check(row,column,size):
    if row + size > 10 or column + size > 10: # 한 네모 종이가 전체 크기보다 큰 경우
        return False

    for i in range(row,row+size):
        for j in range(column, column + size):
            if M[i][j] != 1: # 한 종이로 덮었는데, 1이 아닌게 있는 경우
                return False

    return True # 위의 모든 조건을 다 거쳤을 때 True 반환


def backtrack(pos,used): # 현재 위치, 사용한 색종이 수
    global result

    if pos == 100: # 모눈 종이 1x1의 가장 끝 부분
        result = min(result, used) # 기록되어 있던 최솟값과, 이번 분기에 사용한 종이수 중 작은 것
        return

    if used >= result: #기록되어 있던 최솟값보다 크면 가지치기
        return 

    row,column = divmod(pos,10)  # divmod를 통해 pos 나누기 10을 한 몫과 나머지를 반환

    if M[row][column] == 1: # 시작점 위치의 값이 1인 경우
        for size in range(5,0,-1): # 크기가 5,4,3,..1의 종이까지 체크한다.
            if S[size] > 0 and check(row,column,size): # 사이즈 종이가 아직 남아있고, check도 True일 때

                S[size] -= 1 # 그 크기의 종이를 한번 쓴다.
                
                fill(row,column,size,0) # 종이의 크기만큼 0으로 채운다
                
                backtrack(pos + 1, used + 1) # 다음 위치로 이동해서 재귀한다.
                
                fill(row,column,size,1) # 안됐을 경우, 다시 복구시킴
                
                S[size] += 1 # 썻었던 종이도 다시 돌려놓음


    else:
        backtrack(pos + 1, used) # 위치를 + 1 옮기고 다시 백트래킹 시작


backtrack(0,0) # 0,0부터 시작해서 backtrack 안의 pos까지 돈다.

print(result if result !=float('inf') else -1) # result가 inf가 아니면 result 반환, 그렇지 않다면 -1 반환



