# 1. 변수 선언 및 입력값 받기 

import sys
input = sys.stdin.readline


N = int(input()) # 일하는 날

# N+1일차에 퇴사함
T = [0] * (N+2) # 상담을 완료하기 위해 걸리는 시간
P = [0] * (N+2) # 상담할 때 받을 수 있는 금액

# D[i] : i일차 일 떄 최대 수익
D = [0] * (N+2)


# T,P 입력값 받기

for i in range(1,N+1):
    time,profit = map(int,input().split())
    T[i] = time
    P[i] = profit


# DP 배열 채우기

for i in range(1,N+1):
    # i일일 때 일하지 않았을 경우

    D[i+1] = max(D[i],D[i+1])

    # i일차에 일을 했을 경우

    time_spend = T[i]

    if i + time_spend <= N+1:
        # 돈이 들어오는 '미래의 날짜' 장부에 기록
        D[i+time_spend] = max(D[i+time_spend], D[i] + P[i])



print(D[N+1])