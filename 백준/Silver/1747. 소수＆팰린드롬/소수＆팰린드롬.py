# 문제 42 소수 & 팰린드롬 수 중에서 최솟값 찾기 - 1747번

"""
팰런드롬 판별 함수 구현

팰런드롬 함수:
    숫잣값을 리스트 형태로 변환
    s(시작 인덱스), e(끝 인덱스)
    while s < e:
        만약 시작과 끝 인덱스에 해당하는 값이 다르면 return False
        s값 증가
        e값 감소
        
    반복문을 다 돌았으면 return True

while True:
    N부터 값을 1씩 증가시키면서 A[i]값이 소수이면서 팰린드롬 수인지 판별
    맞으면 반복문 종료

"""

import sys
input = sys.stdin.readline


# 에라토스테네스의 체를 통한 소수 구하기
limit = 2000000 + 1

is_prime = [True] * limit
is_prime[0] = False
is_prime[1] = False

# 배수들을 제거하는 '살수'의 역할을 제곱근까지만 맡긴다
for i in range(2,int(limit**0.5)+1):
    if is_prime[i]:

        for j in range(i*i,limit,i):
            is_prime[j] = False

# N 입력 받기

N = int(input())


# def isPalindrome(num):
#     temp = list(str(num))

#     s = 0
#     e = len(temp) -1

#     while s < e:
#         if temp[s] != temp[e]:
#             return False

#         s +=1
#         e -=1

#     return True


# 어떤 수 N보다 크거나 같고 소수이면서 팰런드린 수 찾기
target = N

while True:
    if is_prime[target] != False:
        if str(target) == str(target)[::-1]: # 글자 거꾸로 뒤집
            print(target) # 가장 먼저 나온게 가장 최소의 값
            break
    
    target +=1
