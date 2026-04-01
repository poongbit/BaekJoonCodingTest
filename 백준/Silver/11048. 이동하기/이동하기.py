import sys
input = sys.stdin.readline
from collections import deque


N,M = map(int,input().split())

graph = []

for i in range(N):
    line = list(map(int,input().split()))
    graph.append(line)

"""
우, 대각선, 아래 이동

dp[i][k] : i row k column에 있을 떄 가질 수 있는 사탕의 최대 개수

dp[0][0] = graph[0][0]

우측 이동 : 
dp[0][1] = dp[0][0] + graph[0][1]
dp[0][2] = dp[0][1] + graph[0][2]
dp[0][3] = dp[0][2] + graph[0][3]


dp[N][i] = dp[N][i-1] + graph[N][i]


아래로 이동
dp[1][0] = dp[0][0] + graph[1][0]
dp[2][0] = dp[1][0] + graph[2][0]
dp[3][0] = dp[2][0] + graph[3][0]


dp[i][M] = dp[i-1][M] + graph[i][M] 


대각선 이동
dp[1][1] = dp[0][1] + graph[1][1] or dp[1][0] + graph[1][1]
dp[2][2] = dp[1][2] + graph[2][2] or dp[2][1] + graph[2][2]


dp[i][i] = dp[i-1][i] + graph[i][i] 
            or dp[i][i-1] + graph[i][i]

            
"""

dp = [[0]*M for _ in range(N)]

dp[0][0] = graph[0][0]


# 0번쨰 열과 0번째 행은 값을 계속 채워나갈 수 있음

# 0번째 열에서 행 채워나가기
for i in range(1,M):
    dp[0][i] = dp[0][i-1] + graph[0][i]

# 0번쨰 행에서 열 채워나가기
for j in range(1,N):
    dp[j][0] = dp[j-1][0] + graph[j][0]


for row in range(1,N):
    for column in range(1,M):
        dp[row][column] = max(dp[row-1][column],dp[row][column-1]) + graph[row][column]


print(dp[-1][-1])
