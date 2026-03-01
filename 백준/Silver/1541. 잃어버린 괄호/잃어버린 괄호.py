# 문제 39 최솟값을 만드는 괄호 배치 찾기 - 1541번

"""
가능한 큰 수를 만들기 위해, 더하기 연산을 모두 계산 한 후에 뺄쎔 연산을 한다.

answer : 정답 변수
A 리스트(들어온 데이터를 "-" 기호를 기준으로 split() 수행)

# 현재 String에 있는 수를 모두 더하는 함수 구현

mySum():
    현재 들어온 String값을 "+" 기호 기준으로 split() 수행
    for 나뉜 데이터 개수 만큼 반복:
        String값을 Integer형으로 변환해 변환값에 더하기

    전체 합 반환

for i를 A만큼 반복:
    결괏값 = mySum(A[i]) 함수 수행하기
    if 가장 앞 데이터일 때:
        answer에 결괏값 더하기

    else:
        answer에서 결괏값 빼기


answer 출력

"""

import sys
input = sys.stdin.readline

answer = 0 # 정답 변수

A = list(map(str,input().split('-')))

def MySum(i):

    data = str(i).split("+") # MySum의 매개 변수를 str로 불러와서 split을 + 기준으로 한다.

    sum = 0

    for i in data:
        sum += int(i)

    return sum


for i in range(len(A)):
    temp = MySum(A[i])

    if i == 0:
        answer += temp # 가장 앞에 있는 값을 더하기

    else:
        answer -= temp # 뒷부분의 값은 합쳐서 빼기

print(answer)
