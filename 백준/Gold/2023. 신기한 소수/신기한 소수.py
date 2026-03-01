# 문제 24 : 신기한 소수 찾기 - 2023번

"""

N(자릿수)

#소수 구하기 함수
for i in range(2,현재 수/2+1):
    if 현재 수 % i가 0이면:
        return 소수가 아님

# DFS 구현
DFS(숫자):
    if 자릿수 == N:
        현재 수 출력

    else
        for i를 1~9 반복:
            if i를 뒤에 붙인 새로운 수가 홀수이면서 소수일 때 # 소수 구하기 함수 사용
                DFS(수 * 10 + 뒤에 붙는 수) 실행


DFS 실행 (숫자 2,3,5,7로 탐색 시작)

"""

import sys
sys.setrecursionlimit(10000)

input = sys.stdin.readline
N = int(input())

def isPrime(num):
    for i in range(2, int(num **0.5 + 1)):
        if num % i == 0:
            return False

    return True


def DFS(number):
    if len(str(number)) == N:
        print(number)

    else:
        for i in range(1,10):
            if i % 2 == 0:
                continue

            if isPrime(number * 10 + i):
                DFS(number * 10 + i) # N자리까지 재귀 함수 형태로 탐색


# 일의 자리 소수는 2,3,5,7이므로 4가지 수에서만 시작

DFS(2)
DFS(3)
DFS(5)
DFS(7)


