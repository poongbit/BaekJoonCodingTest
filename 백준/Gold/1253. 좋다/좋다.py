# 1. 입력값 받기

import sys
input = sys.stdin.readline
N = int(input())
numbers = list(map(int,input().split()))

# 2. numbers를 O(nlogn) 시간 복잡도로 정렬 (number.sort() 사용)
numbers.sort()

# 3. numbers 안에 숫자들을 하나씩 돌리면서, 두 포인터로 좋은 수 찾기

result = 0 # 좋은 수의 개수 카운팅


for i in range(N):
    find = numbers[i]
    
    # 매 인덱스 마다, 두 포인터 초기화
    left_point = 0
    right_point = N-1
    
    while left_point < right_point:
        if numbers[left_point] + numbers[right_point] == find:
            # 0이 있는 경우, 한 쪽은 같은 수를 더해서 find를 찾으므로 조건을 걸어야 함
            if left_point != i and right_point != i:
                result +=1
                break # 이제 찾았으니, 다음 for 반복 부분으로 넘어감
                
            elif left_point == i:
                left_point +=1 # 왼쪽 포인터가 자기 자신일 경우, 오른쪽으로 이동
                
                
            elif right_point == i:
                right_point -=1 # 오른쪽 포인터가 자기 자신일 경우, 왼쪽으로 이동
                
                
        elif numbers[left_point] + numbers[right_point] < find:
            left_point +=1 # 왼쪽 포인터를 오른쪽으로 한 칸 이동시켜 조금씩 숫자를 크게 만든다.
            
            
        else:
            right_point -=1 # 오른쪽 포인터를 왼쪽으로 한 칸 이동시켜 조금씩 숫자를 작게 만든다.
            
            
print(result)
                
