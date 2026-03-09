# 백준 13251 - 조약돌 꺼내기

import sys
input = sys.stdin.readline

"""
M : 조약돌 색상 종류
N ; 조약돌 정보
K : 뽑은 횟수

"""
# 1. 입력값 받기

M = int(input())

N = list(map(int,input().split()))

K = int(input())


all_rocks = sum(N)



dp = [[0]*(all_rocks + 1) for _  in range(all_rocks + 1)]

for i in range(all_rocks+1):
    dp[i][0] = 1
    dp[i][i] = 1


for i in range(2,all_rocks+1):
    # j를 i까지 가지 말고 K까지만 가게 한다.
    for j in range(1,min(i,K+1)):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

# 전체 경우의 수 구하기 
all_probs = dp[all_rocks][K]


# 같은 색의 돌만 뽑는 경우
color_probs = 0

for i in range(len(N)):
    color_probs += dp[N[i]][K]

print(color_probs/all_probs)

