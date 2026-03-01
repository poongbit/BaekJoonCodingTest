# 문제 34 - K번째 수 1300번
"""
N : 배열의 크기 (N * N 구구단 표)
K : 우리가 찾고 싶은 'K번째' 순서

# 1. 이진 탐색의 양쪽 끝점 설정

start = 1

# K번째 숫자는 절대 K를 넘을 수 없음!
구구단 1단만 있을 때는 K번째 숫자는 K이지만,
다른 단이 들어 올 때 무조건 K보다 작거나 같은 숫자들이 비집고 들어가기 떄문에,
K번째에 있는 숫자는 무조건 K보다 작거나 같음


end = K 

result = 0 # 정답을 기록할 변수

# 본격적인 업 앤 다운 스무고개 시작
while start <= end:
    mid = (start + end) // 2 # 이번엔 정답을 mid라고 찍기

    # 핵심로직 : 이 mid보다 작거나 같은 숫자가 구구단 표에 몇 개나 있을까?
    count = 0

    for i in range(1,N+1): # 1단부터 N단까지 한 줄 씩 검사
        # i단에서 mid보다 작거나 같은 수의 개수 = 몫 (mid // i)
        # 단, N열까지 있으므로 개수가 N을 넘지는 못함
        count += min(mid // i, N)


    #판정 시간

    
    if count < K:
        # mid보다 작거나 같은 숫자를 다 세어볼 때 K가 안되는 경우:
        # 찍은 숫자(mid)가 너무 작다는 뜻이므로 키워야 함,Up

        start = mid + 1

    else : # count >= K
        # 개수가 K개 이상이긴 하네, 그럼 이 mid가 정답 후보가 될 수 있겠다.
        result = mid

        # 하지만 조건을 만족하는 숫자 중에서 '가장 작은 수'를 찾아야 하니 더 쥐어 짜보기, Down
        end = mid - 1

# 스무고개 끝나고 살아남은 최종 정답 출력
출력 (result)

"""

import sys
input = sys.stdin.readline

N = int(input())
K = int(input())


start = 1
end = K
result = 0 


while start <= end:

    mid = (start + end) // 2

    # 이 mid보다 작거나 같은 숫자들이 몇 개나 있을 까?
    count = 0

    for i in range(1,N+1): # 구구단 1단부터 N단까지 확인

        # i단에서 mid보다 작거나 같은 숫자들의 개수
        # N열까지 있으므로 개수 N개는 넘지 못함 (ex) 3*3 배열에서 mid = 4인 경우, 4//1 = 4지만, (1,2,3) 총 3개임
        count += min(mid// i, N)

    # 판정 시간
    if count < K:
        # mid보다 작거나 같은 숫자를 셌을 때 K개가 안됨
        # 너무 작은 숫자를 찍었으므로 숫자 키우기 Up
        start = mid + 1

    else: # count >= K
        # 개수가 K개 이상이므로 mid가 정답 후보가 될 수 있음
        
        result = mid

        # 조건을 만족하는 숫자들 중에, 가장 작은 수를 찾아야 하므로, 더 쥐어짜보기 Down

        end = mid -1


print(result)
