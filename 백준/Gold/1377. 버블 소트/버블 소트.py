# 문제 16 : 버블 정렬 프로그램

"""
N(데이터 개수), A(데이터 리스트, 단 클래스를 데이터로 담는 리스트)


for N만큼 반복:
    A 리스트 저장


A 리스트 정렬


for N만큼 반복:
    A[i]의 정렬전 index - 정렬 후 index 계산의 최댓값을 찾아 저장


"""

import sys
input = sys.stdin.readline

N = int(input())

A = [] # 데이터 리스트 (값, 인덱스) 튜플로 받기


# 데이터 입력 받기
for i in range(N):
    # 데이터 값과 인덱스를 튜플로 받아서, 나중에 sorted 될 떄의 index 위치랑 비교할 예정
    tupled = (int(input()),i)
    A.append(tupled)




max = 0
sorted_A = sorted(A)



for i in range(N):

    if max < sorted_A[i][1] - i:  # 여기서 i는 정렬된 후의 인덱스를 가리킴
        max = sorted_A[i][1] - i



# 제대로 swap이 다 됐는 지 한번 더 돔
print(max+1)

