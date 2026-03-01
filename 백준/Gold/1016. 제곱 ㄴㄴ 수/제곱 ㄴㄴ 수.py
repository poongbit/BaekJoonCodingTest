# 문제 43 제곱이 아닌 수 찾기 - 1016번 

"""
min,max 입력받기

A = [True] * (max - min + 1) # 딱 필요한 구간만 100만 개 짜리로 아담하게 생성

실수(i)를 2부터 시작해서 제곱수(i*i)가 max보다 작거나 같을 때까지 반복:
    제곱수 = i * i

    # min 이상인 '첫 번째 제곱수의 배수' 의 시작점 찾기

    start = min // 제곱수

    만약 min % 제곱수 !=0 이라면, # 딱 안 떨어지면 몫을 1 올려줌
        start +=1

    
    진짜_시작숫자 = start * 제곱수

    # 찾아낸 시작 숫자부터 max까지, 제곱수 보폭으로 점프하면서 삭제

    for j in range(진짜_시작숫자,max + 1, 제곱수):
        방번호(인덱스) = j - min # 진짜 숫자에서 min을 빼면 우리 배열의 방 번호가 됨 / 평행이동 스킬

        A[방번호]= False


A 배열에서 끝까지 True로 살아남은 놈들의 개수를 출력


어떤 수를 무조건 올림하고 싶다?
몫 = (A + B -1) // B


"""
import sys

input = sys.stdin.readline

# 1. 입력 받기

min_val, max_val = map(int,input().split())

# 2. 필요한 구간만 생성하기

A = [True] * (max_val- min_val + 1)


for i in range(2,int(max_val**0.5) + 1): # 제곱근까지 체크
    pow_val = i * i

    # min 이상인 '첫 번째 제곱수의 배수'의 시작점 찾기
    start = min_val // pow_val

    if min_val % pow_val != 0: # 딱 안 떨어지면 몫을 1 올림
        start +=1

    real_start = start * pow_val

    # 찾아낸 시작숫자부터 max까지, 제곱수 보폭으로 점프하면서 삭제

    for j in range(real_start, max_val + 1, pow_val):
        room_index = j - min_val # 진짜 숫자에서 min을 빼면 방 배열번호가 됨, 평행이동
        A[room_index] = False


count = 0

for i in range(0,max_val-min_val+1):
    if A[i]:
        count +=1

print(count)