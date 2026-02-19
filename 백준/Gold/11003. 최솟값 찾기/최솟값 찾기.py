# 문제 10 최솟값 찾기

"""
N개의 수  A1, .. An /

L번째 ~ i번쨰 중 최솟값을 D라고 할 떄, D에 저장된 수를 출력하는 프로그램은?

N(데이터 개수), L(최솟값을 구하는 범위)
mydeque(데이터를 담을 덱 자료구조)
now (주어진 숫자 데이터를 가지는 리스트)


for N만큼 반복: # now 리스트를 탐색 (now[i]를 현재 값으로 설정)
    덱의 마지막 위치에서 현 재 값보다 큰 값은 덱에서 제거
    덱의 마지막 위치에 현재 값 저장
    덱의 1번째 위치에서 L의 범위를 벗어난 값(index <= now index - L)
    덱의 1번째 데이터 출력

"""
# 데이터 불러오기

import sys
input = sys.stdin.readline

from collections import deque

N,L = map(int,input().split())
numbers = list(map(int,input().split()))

mydeque = deque()



# 새로운 값이 들어올 때마다 정렬 대신 현재 수보다 큰 값을 덱에서 제거해 시간 복잡도를 줄임
for i in range(N):
    
    # 맨 뒤의 deque에서의 값 불러오기
    while mydeque and mydeque[-1][0] > numbers[i]: # deque가 있는 경우, 그리고 deque 맨 뒤의 값이 numbers보다 큰 경우
        mydeque.pop()


    mydeque.append((numbers[i],i)) # 나중에 뒤따라올 숫자들 크기 비교를 위해 저장 / 자신의 위치표 달기 위함

    if mydeque[0][1] <= i-L: # L부터 i까지의 범위에서 벗어난 값은 덱에서 제거
        mydeque.popleft() #0번째 deque에서 인덱스 값 꺼내기


    print(mydeque[0][0], end = ' ') # 가장 맨 앞의 데이터가 최소이므로 보여준다.

 


