# 문제 37 수를 묶어서 최댓값 만들기 1744번

"""
N : 수열의 크기
plus_list = []  # 1보다 큰 양수
minus_list = [] # 음수
ones_count = 0 # 1의 개수
zeros_count = 0 # 0의 개수

# 1. 숫자들을 4가지 파벌로 분류하기

N만큼 반복:
    숫자 입력받기

    if 숫자 > 1:
        plus_list에 추가

    elif 숫자 == 1:
        ones_count 1 증가

    elif 숫자 < 0:
        minus_list에 추가
    
    else: #숫자가 0인 경우
        zeros count 1 증가


# 2. 끼리끼리 곱했을 때 최대 시너지를 내기 위한 정렬
plus_list 정렬 (내림차순) : 큰 수부터 묶어야 하기 위함, ex) 5,4,3...
minus_list 정렬 (오름차순) : 마이너스가 큰(작은 수) 놈들부터 묶어야 하니까 -5,-4,-3...

최종_점수 = 0

# 3. 양수 묶어주기

while plus_list의 길이가 2 이상일 때:
    가장 큰 수 두 개를 리스트에서 꺼냄 (pop 2번)
    최종_점수 += (꺼낸 두 수의 곱)


만약 plus_list에 1개가 남았다면:
    최종_점수 += 남은 1개의 수(혼자 더하는게 최선)

# 4. 음수 묶어주기

while minus_list의 길이가 2 이상일 때:
    가장 작은 수 두 개를 리스트에서 꺼냄 (pop 두번)
    최종 점수 += 꺼낸 두 수의 곱, # 음수 * 음수 = 양수

만약 minus_list에 1개가 남았다면:
    if zeros_count == 0: #
        최종 점수 += 남은 1개의 수 # 어쩔 수 없이 남은건 더해줌

    만약 zeros count가 0보다 크면?
    --> 0이랑 곱해서 폭파시킬 수 있으므로, 아무것도 안 더하고 그냥 버림


# 5. 1 더하기
최종 점수 += ones_count # 1은 무조건 곱하지 않고 더하는게 이득!

# 최종 결과 출력
출력(최종점수)

"""
# heap은 가장 작은 수부터 튀어나오는 최소 힙(Min-heap)
# 그래서 양수 그룹은 가장 큰 수부터 튀어나오게 하기 위해, 마이너스(-)를 붙혀서 넣는 '최대 힙 꼼수'를 쓴다.


import sys
input = sys.stdin.readline

import heapq

N = int(input())

plus_pq = [] # 1보다 큰 양수
minus_pq = [] # 음수
ones_count = 0 # 1의 개수
zeros_count = 0 # 0의 개수


# 1. 숫자 입력 받기
for i in range(N):
    number = int(input())

    if number > 1:
        # 양수는 가장 큰 놈부터 튀어나오게 하려고 음수로 둔갑시켜서 넣기!
        heapq.heappush(plus_pq,-number)

    elif number == 1:
        ones_count +=1

    elif number == 0:
        zeros_count +=1

    else: # 음수인 경우
        # 음수는 원래 작은 놈(마이너스가 큰 놈)부터 꺼내야 하니 그대로 넣음!
        heapq.heappush(minus_pq,number)


total_sum = 0

# 2. 양수 꺼내기

while len(plus_pq) > 1:
    # 꺼낼 때는 다시 마이너스를 붙혀서 원래의 양수로 원상 복구!
    temp1 = -heapq.heappop(plus_pq)
    temp2 = -heapq.heappop(plus_pq)

    total_sum += (temp1 * temp2)

if len(plus_pq) == 1:
    total_sum += -heapq.heappop(plus_pq) # 그냥 더해준다.


# 3. 음수 묶어주기

while len(minus_pq) > 1:
    # 가장 작은 수끼리 곱해주면, 가장 큰 양수가 됨

    temp1 = heapq.heappop(minus_pq)
    temp2 = heapq.heappop(minus_pq)

    total_sum += (temp1 * temp2)

if len(minus_pq) == 1: # 만약 1개 홀수 개로 남았다면
    leftover = heapq.heappop(minus_pq)

    if zeros_count == 0: # 0이 하나도 없다면, 어쩔 수 없이 더해줌
        total_sum += leftover

    # 만약 없다면, 곱하면 0가 되므로 굳이 안 더해도 됨

# 4. 1 더해주기
total_sum += ones_count

print(total_sum)

