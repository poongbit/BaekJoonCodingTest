# 문제 15. 수 정렬하기 1

"""
N (정렬할 수 개수)
A(수 저장 리스트 선언 및 입력 데이터 저장)

for i를 0 ~ N-1만큼 반복:
    for j를 0~ N-1-i만큼 반복:
        현재 A 리스트의 값보다 1칸 오른쪽 리스트의 값이 더 작으면 두 수를 바꾸기

A 리스트 출력

"""

import sys

input = sys.stdin.readline

n = int(input())
A = [0] * n


# 입력값 받기
for i in range(n):
    A[i] = int(input())


for i in range(n-1): # 0 ~ n-2 까지
    for j in range(n-1-i): # 0부터 n-1-i까지 / i가 증가할 수록, 우측에 이미 정렬된 부분은 빼고 swap될 예정
        if A[j] > A[j+1]:

            # 바로 swap 하기

            temp = A[j]
            A[j] = A[j+1]
            A[j+1] = temp


for i in range(n):
    print(A[i])

