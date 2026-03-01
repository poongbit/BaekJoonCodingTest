# 문제 42 소수 & 팰린드롬 수 중에서 최솟값 찾기 - 1747번



import sys
input = sys.stdin.readline


# 에라토스테네스의 체를 통한 소수 구하기
#limit은 '문제에서 주어질 수 있는 최악의 정답치'를 예상해서 아주 살짝만 여유 있게 잡는다! 
#(모르겠으면 입력 최댓값의 1.5배 ~ 2배 정도)

limit = 1500000 + 1

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



# 어떤 수 N보다 크거나 같고 소수이면서 팰런드린 수 찾기
target = N

while True:
    if is_prime[target] != False:
        if str(target) == str(target)[::-1]: # 글자 거꾸로 뒤집
            print(target) # 가장 먼저 나온게 가장 최소의 값
            break
    
    target +=1

