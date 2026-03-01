# 문제 33 기타 레슨  - 2343번

"""
N: 강의의 수
M : 블루레이의 수
A : 강의 시간 데이터 리스트

# 1. 탐색의 양쪽 끝점(최소,최대 크기) 절대 기준 세우기 

start = A 배열의 최댓값, 아무리 상자를 줄여도, 제일 긴 강의 하나는 들어가야 함
end = A 배열의 모든 합, # 상자 1개의 모든 강의를 다 떄려 넣는 최악(?)의 경우

result = 0, 정답(최소 블루레이 크기)을 기록할 변수

#2. 이진 탐색

whlie start <=end:
    mid = (start + end) // 2 # 이번 판 블루레이 크기를 mid로 가정

    # 이 mid 크기로 블루레이가 몇 장 필요한지 직접 세어보기
    count = 1 # 일단 블루레이 1장 꺼내놓고 시작
    current_sum = 0 # 현재 블루레이에 담은 강의 시간의 합

    for i in range(N):
        # 만약 '지금까지 담은 시간 + 이번 강의 시간'이 상자 크기(mid)를 넘친다면?
        if current_sum + A[i] > mid:
            count +=1 # 꽉 찼으니 새 블루레이 상자 하나 더 꺼내오기
            current_sum = A[i] # 새 상자에 이번 강의를 넣음


        # 아직 상지에 자리가 넉넉하다면
        else:
            current_sum += A[i] # 현재 상자에 계속 강의를 담음

    
    # 3. 판정하기
    if count > M:
        # M장 안에 다 담아야 하는데, 상자가 너무 작아서 M장보다 더 많이 썼다.
        # 상자 크기를 키워야 함 (Up)
        start = mid + 1


    else:
        # 일단  M장(혹은 그 이하) 안에 충분히 다 담기긴 함
        # 일단 성공했으니 후보로 기록하기
        result = mid

        # 그래도 상지 크기를 더 빡빡하게 줄여도 될까 하고 작은 쪽을 탐색 (Down)
        end = mid - 1

# 스무고개 다 끝나고 살아남은 최적의 크기를 출력

출력 result

"""

import sys
input = sys.stdin.readline

N,M = map(int,input().split()) # N,M 입력받기

A = list(map(int,input().split())) # A 입력 받기


start = max(A)
end = sum(A)

result = 0 


while start <= end:
    mid = (start + end) // 2

    # mid 크기로 블루레이가 몇 장이나 들어가나?
    count = 1 # 블루레이 1장 꺼내놓고 시작
    current_sum = 0 # 현재 블루레이에 담은 강의 시간의 합

    for i in range(N): # 강의의 수 만큼 반복
        if current_sum + A[i] > mid:
            count +=1 # cd 한장 더 필요함
            current_sum = A[i] # 새 상자에 이번 강의를 넣음

        
        # 아직 상자 널널함?
        else:
            current_sum += A[i]

    
    # 판정 시간
    if count > M:
        # M장 안에 담기로 했는데, M장보다 많이 씀
        # 상자 크기 더 키우기!
        start = mid + 1

    else:
        # M장 안에 충분히 다 담김
        # 일단 성공했으니 정답 후보로 기록
        result = mid

        # 상자 크기를 더 빡빡하게 줄여도 될 지 하고 더 작은 쪽 탐색
        end = mid - 1

print(result)