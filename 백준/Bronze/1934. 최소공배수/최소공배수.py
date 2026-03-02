# 문제 45 - 최소 공배수 구하기 - 1934번

"""

최소 공배수 구하기

A * B = 최대 공약수 * 최소 공배수 (소인수 분해 구했던 그 방식 생각하면 됨)

따라서 최소 공배수 = (A * B) // 최대 공약수


"""

import sys
input = sys.stdin.readline

# 테스트 횟수 입력 받기
T = int(input())


# 최대공약수 구하는 함수 구현

def gcd(A,B):
    # 나누는 수가 0이면, 그 나누는 수가 최대 공약수가 됨

    if B == 0:
        return A

    #굳이 if문으로 나누지 않아도, 
    #알아서 큰 수가 앞으로, 작은 수가 뒤로 자리를 바꿔버림
    else:
        return gcd(B, A % B)


for _ in range(T):
    A,B = map(int,input().split())

    result = (A * B) // gcd(A,B)

    print(result)
