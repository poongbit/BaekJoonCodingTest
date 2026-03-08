import sys
input = sys.stdin.readline

Q = int(input())

for _ in range(Q):
    N,M = map(int,input().split())
       
    dp = [[0]*(M+1) for _ in range(M+1)]
    
    for i in range(M+1):
        dp[i][0] = 1
        dp[i][i] = 1
        
    for i in range(2,M+1):
        for j in range(1,i):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
            
    print(dp[M][N])
