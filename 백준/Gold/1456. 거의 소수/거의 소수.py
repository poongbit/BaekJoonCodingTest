# 문제 41 거의 소수 구하기 - 1456번

"""
A : 시작 범위
B : 종료 범위

# 1. 에라토스테네스의 체 가동
10^7까지의 소수들을 싹 다 구해서 'primes'라는 리스트에 담아둔다.

정답_카운트 = 0

# 2. 소수 명단에서 한 놈씩 꺼내서 뻥튀기 검사 시작

for P in primes:
    #처음 검사할 '거의 소수'는 P의 제곱부터 시작

    현재_값 = P*P

    # 뻥튀기한 값이 B를 뚫고 나가지 않을 때까지 무한 반복
    while 현재_값 <= B:

        # 만약 이 뻥튀기 값이 A 범위 안으로 들어왔다면, 정답
        if 현재_값>=A:
            정답 카운트 +=1

        # 다음 검사를 위해 P를 한번 더 곱해줌 (P^2, P^3, P^4....)
        현재값 = 현재값 * ㅖ

최종 정답 카운트 출력


"""

import sys
input = sys.stdin.readline

A,B = map(int, input().split())

# 1. 최대 범위 B의 제곱근까지만 '체'를 만든다. (최대 10^7)
limit = int(B**0.5) + 1

is_prime = [True] * limit
is_prime[0] = False
is_prime[1] = False

# 2. 에라토스테네스의 체 만들기
for i in range(2,int(limit**0.5) + 1):
    if is_prime[i]:
        
        # i*2 가 아니라, i*i부터 지우면 중복을 없애 훨씬 빠르다
        for j in range(i*i, limit, i):
            is_prime[j] = False

answer = 0


# 3. 명단에서 소수를 하나씩 꺼내서 P의 N제곱(N>1)씩 검사
for i in range(2,limit):
    
    # i가 살아있는 소수일 때
    if is_prime[i]:
        current = i * i # 첫 '거의 소수'는 P^2부터 시작

        # 4. 제곱된 값이 B를 뚫고 나가지 않을 때까지 무한 반복
        while current <= B:
            # 제곱된 값이 목표 범위 A 이상이라면 정답 카운트 + 1
            if current >= A:
                answer +=1

            # 다음 제곱을 위해 P(i)를 한 번 더 곱해줌 (P^2, P^3, ...)
            current *= i


print(answer)