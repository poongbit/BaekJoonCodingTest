import sys
input = sys.stdin.readline

N = int(input().strip())

# dp[i][1] : i번쨰 계단으로 올 떄, i-1번째 계단은 안 밟고 온 최댓값
# dp[i][2] : i번째 계단일 떄, i-1번째 계단을 밟고 온 최댓값

dp = [[0]*3 for _ in range(N+1)]

stair = [0] # 1-based index를 위함

for _ in range(N):
    num = int(input().strip())
    stair.append(num)

# 0번째 계단을 안 밟고 옴
dp[1][1] = stair[1]

# i-1번째 계단을 밟을 수 없음
dp[1][2] = 0


if N>=2:
    dp[2][1] = stair[2]
    dp[2][2] = dp[1][1] + stair[2]


for i in range(3,N+1):
    dp[i][2] = dp[i-1][1] + stair[i]
    dp[i][1] = max(dp[i-2][1],dp[i-2][2]) + stair[i]

print(max(dp[N][1],dp[N][2]))





