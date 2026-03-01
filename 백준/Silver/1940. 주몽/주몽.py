# 문제 7 주몽의 명령

"""
2가지 재료의 고유한 번호 -> M


N개의 재료, M ->  갑옷 몇개?

6 : 재료의 개수
9 ; 갑옷이 완성되는 번호의 합

2 7 4 1 5 3 --> 2


수도 코드

N : 재료의 개수
M : 두 재료를 합쳐서 나와야 하는 숫자

numbers : 재료들을 담는 리스트


1) numbers의 리스트를 정렬한다

2) 투 포인터를 이용해서 하나 하나씩 더한다.



A[i] + A[j] > M : j-- # 번호의 합이 M보다 크므로 큰 번호 index를 내린다
A[i] + A[j] < M : i++ # 번호의 합이 M보다 작으므로 작은 번호 index를 올린다
A[i]+ A[j] == M : i++, j--, count +=1, # 양쪽 포인터를 모두 이동시키고, count를 증가시킨다.



"""

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

# 리스트를 받고 오름차순으로 정렬하기
numbers = list(map(int,input().split()))
numbers.sort()

# 투 포인터 지정

left_point = 0
right_point = len(numbers)-1

# 답을 카운트할 변수 초기화
count = 0

while left_point < right_point:
    if numbers[left_point] + numbers[right_point] == M:
        count +=1
        left_point +=1
        right_point -=1

    elif numbers[left_point] + numbers[right_point] < M:
        left_point +=1

    else:
        right_point -=1


print(count)