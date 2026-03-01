# 문제 36 - 카드 정렬하기 1715번

"""
N : 카드 묶음 개수
pq : 우선 순위 큐

for N만큼 반복:
    우선순위 큐에 데이터 저장

# 자동정렬에 따라 작은 카드 묶음 2개를 쉽게 뽑을 수 있음
while 우선수위 큐 크기가 1이 될때까지:
    2개 카드 묶음을 큐에서 뽑음
    2개 카드 묶음을 합치는데 필요한 비교 횟수를 결괏값에 더함
    2개 카드 묶음의 합을 우선순위 큐에 다시 넣음

결괏값 출력

"""

import sys
import heapq
input = sys.stdin.readline

N = int(input())
pq = [] # heapq는 일반 리스트 사용

# 1. 항아리에 데이터 넣기

for _ in range(N):
    data = int(input())
    heapq.heappush(pq,data) # pq라는 리스트에 data를 넣으면서 자동 정렬 (put 역할)

total_sum = 0

# 2. 두 개씩 꺼내서 합치기
while len(pq)> 1: # 두 팩 이상 남아 있는 경우
    data1 = heapq.heappop(pq) # 제일 작은 거 뽑기 (get 역할)
    data2 = heapq.heappop(pq) # 두 번쨰로 작은거 뽑기

    temp = data1 + data2 # 두 묶음 합치기
    total_sum += temp # 비교 횟수 누적

    heapq.heappush(pq,temp) # 합친 덩어리를 pq 리스트에 temp에 던저 넣기 (put 역할)


print(total_sum)