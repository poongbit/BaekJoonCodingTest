import sys
input = sys.stdin.readline

n,k = map(int,input().split())

coins = []

for _ in range(n):
    coin = int(input().strip())

    coins.append(coin)

"""
dp[k] : k원이 되기 위해 필요한 동전의 개수

"""

INF = float('inf')

dp = [INF] *(k+1)

# 0원을 만들 수 있는 동전의 개수 - 0개
dp[0] = 0

for coin in coins:
    for j in range(coin,k+1):
        # j-coin 원에서 동전 1개 추가하면 j원이 도므로
        dp[j] = min(dp[j-coin] +1, dp[j])


if dp[k] == INF:
    print(-1)

else:
    print(dp[k])