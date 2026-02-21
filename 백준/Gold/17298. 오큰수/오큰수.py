# 문제 12 : 오큰수 구하기

"""
크기가 N인 수열 A = A,...An

Ai의 오큰수 : 오른쪽에 있으면서 Ai보다 큰 수 중 가장 왼쪽에 있는 수

N : 수열의 크기
numbers = 숫자 크기

nge_num = 0 # 0번쨰부터 비교하기

[3,5,2,7]


"""

import sys
input = sys.stdin.readline

n = int(input()) # 수열의 크기
ans = [0] * n # 정답 리스트

A = list(map(int,input().split())) # 수열을 받을 코드

myStack = [] # 정답 index를 받을 공간


for i in range(n): # n번 반복되는 동안
    # 스택이 비어 있지 않고 현재 수열이 스택 top 인덱스가 가리키는 수열보다 클 경우

    while myStack and A[myStack[-1]] < A[i]:
        ans[myStack.pop()] = A[i] # 정답 리스트에 오큰수를 현재 수열로 저장하기
    myStack.append(i) # 그 i index도 스택에 들어와서 저거보다 더 큰 오큰수가 있는 지 확인


while myStack: # 반복문을 다 돌고 나왔는데 스택이 비어 잇지 않다면 빌 떄까지:
    ans[myStack.pop()] = -1 # 스택에 쌓인 index의 정답 배열에 -1을 넣기 

# 언패킹
print(*ans)


