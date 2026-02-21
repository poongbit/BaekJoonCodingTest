# 문제 18 ATM 인출 시간 계산하기

"""
N : 사람 수
A : 각 사람의 인출 시간을 저장한 리스트
S : A의 합 배열, 각 사람이 인출을 완료하는 데 필요한 시간을 저장


for i를 1~N만큼 반복:
    for j를 i-1 ~ 0까지 뒤에서 부터 반복:
        현재 범위에서 삽입 위치 찾기

    for j를 i~insert_point+1까지 뒤에서 부터 반복:
        삽입을 위해 삽입 위치에서 i까지 데이터를 한 칸씩 뒤로 밀기

    삽입 위치에 현재 데이터 저장


for i 를 1~N만큼 반복:
    A 리스트로 합 배열 S 만들기


S 리스트의 각 데이터값을 모두 합해 결과 출력

"""

import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
S = [0] * N

# insert_point 기준으로 왼쪽이 정렬됨, 오른 쪽이 미 정렬 상태임

for i in range(1,N): #삽입 정렬
    insert_point = i # 삽입할 위치
    insert_value = A[i] # 삽입할 위치에서의 데이터

    for j in range(i-1,-1,-1): # 역순으로 숫자가 줄어들면서 insert_point를 찾는 과정
        if A[j] < A[i]:
            insert_point = j + 1 # 작은 곳 다음 위치에 insert함
            break

        if j == 0:
            insert_point = 0 # 가장 작으므로 0번쨰 자리에 둔다.


    for j in range(i, insert_point, -1): #정렬된 부분에서 위치를 한 칸씩 옮긴다.
        A[j] =  A[j-1]

    A[insert_point] = insert_value


# 합 배열 형성

S[0] = A[0]

for i in range(1,N): # 합배열 만들기
    S[i] = S[i-1] + A[i]


sum = 0

for i in range(0,N): # 합 배열 총합 구하기
    sum += S[i]


print(sum)