# 문제 17 내림차순으로 자릿수 정렬하기

"""
A : 자릿수별로 구분해 저장한 리스트
A 리스트 저장



for i를 A 리스트 만큼 반복:
    for j를 i+1 ~ A 리스트 길이 만큼 반복:
        현재 범위에서 max값 찾기

    현재 i의 값과 max값 중 max값이 더 크면 swap 수행



A 리스트 출력

"""

import sys

input = sys.stdin.readline
print = sys.stdout.write

A = list(input())


for i in range(len(A)): # 왼쪽부터 차례대로 정렬되기 시작함
    max = i # 내림차순 정렬이기 때문에, 왼쪽에 가장 큰 수가 와야 함
    
    for j in range(i+1,len(A)):
        if A[j] > A[max]: # 내림차순이므로 최댓값을 찾음
            max = j

    if A[i] < A[max]:
        temp = A[i]
        A[i] =  A[max]
        A[max] = temp


for i in range(len(A)):
    print(A[i])
