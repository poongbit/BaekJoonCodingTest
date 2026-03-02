# 문제 46번 최대 공약수 구하기 - 1850

"""

수의 길이를 나타내는 두 수의 최대 공약수 

= A,B의 최대 공약수의 길이

gcd로 최대 공약수 구하기

최대 공약수 * '1'의 개수 출력?


"""

import sys

input = sys.stdin.readline

A,B = map(int,input().split())

# gcd 함수 구현

def gcd(A,B):
    if B == 0:
        return A

    else:
        return gcd(B,A % B)


count_1 = "1" * gcd(A,B)

print(str(count_1))

