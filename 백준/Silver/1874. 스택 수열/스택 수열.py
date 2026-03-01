import sys

# 입력값 받기
N = int(input()) # 수열 개수
numbers = [0] * N # 수열 리스트 선언

for i in range(N):
    numbers[i] = int(input()) # 수열 리스트 다 받기
    
stack = [] # 오름차순 자연수가 담길 스택
num = 1 # 오름차순 자연수
result = [] # 스택의 결과 (+,-)가 담길 리스트

is_available = True # 스택으로 수열이 표현 되는 지 여부


for i in range(N):
    su = numbers[i] # 현재 수열 값
    
    if su >= num: # 현재 수열 값이 오름차순 자연수보다 크거나 같다면
        while su >= num:
            stack.append(num) # 오름차순 자연수 하나 추가
            num +=1 #오름차순 자연수 1 증가
            result.append('+')
            
        stack.pop()
        result.append('-')
        
    else: # 현재 수열 값 < 오름차순 자연수
        n = stack.pop()
        if n > su: # 스택 pop 결과값 > 수열의 수
            print("NO")
            is_available = False
            break
            
        else:
            result.append('-')

            
if is_available:
    for i in result:
        print(i)

       
            
            
    



