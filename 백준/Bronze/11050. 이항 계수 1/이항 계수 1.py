import sys
input = sys.stdin.readline

N,K = map(int,input().split())

# 2차원 리스트를 0으로 초기화 (N+1 x N+1 크기)
dp = [[0] * (N+1) for _ in range(N+1)]

for i in range(N+1):
    dp[i][0] = 1  # i개 중에서 하나도 안 뽑을 경우
    dp[i][i] = 1  # i개 중에서 i개 전부 다 뽑을 경우
    

for i in range(2,N+1):
    for j in range(1,i):
        dp[i][j]  = dp[i-1][j-1] + dp[i-1][j]
        
print(dp[N][K])