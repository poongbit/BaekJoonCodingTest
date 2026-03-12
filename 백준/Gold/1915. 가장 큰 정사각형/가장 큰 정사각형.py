import sys
input = sys.stdin.readline


# 1. 입력값 받기, 변수 선언
n,m = map(int,input().split())

master_map = [[0]*(m+1) for _ in range(n+1)]

for i in range(1,n+1):
    row = list(input().strip())

    for j in range(1,m+1):
        master_map[i][j] = int(row[j-1])



# D[i][j] : (i,j)를 우하단 꼭짓점으로 하는 최대 정사각형 변의 길이

D = [[0] * (m+1) for _ in range(n+1)]
max_length = 0

"""


3 x 3 정사각형을 만들려고 할 때, 예를 들어 다른 곳은 다 되는데 왼쪽 위 사격형(D[i-1][j-1])이 길이가 2가 안되는 경우,
3x3을 못 만드므로, 세 사각형 중에 가장 작은 대각선 사걱형을 기준으로 길이가 늘어남


"""



# DP 점화식

for i in range(1,n+1):
    for j in range(1,m+1):

        if master_map[i][j] == 1: # 정사각형 배열 값이 1인 경우

            D[i][j] = min(D[i][j-1],D[i-1][j],D[i-1][j-1]) + 1


            if D[i][j] > max_length:
                max_length = D[i][j]



print(max_length*max_length)
