import sys
input = sys.stdin.readline

n,k = map(int,input().split())

coin = []

for i in range(n):
    value = int(input().strip())

    coin.append(value)

# k원을 만드는 경우의 수
dp = [0] * (k+1)

"""
dp[j] : j원 만드는 경우의 수
# 어쩃든 문제에서 경우의 수를 구해야 함

dp[k] : k원을 만들기 위한 경우의 수

# 경우의 수를 누적
dp[k] += dp[k-c] #인 경우의 수

"""
# 0원으로 만들 가짓 수는 한 가지
dp[0] = 1

for item in coin:
    for j in range(item,k+1):
        dp[j] += dp[j-item]


print(dp[k])
