# 문제 14 절대값 힙 구현하기

"""
N : 질의 요청 개수
우선 순위 큐 선언

- 절댓값 기준으로 정렬되도록 설정
- 단, 절댓값이 같으면 음수 우선 정렬


"""

import sys
import heapq # heap 모듈 불러오기

# 입출력 속도 향상

input = sys.stdin.readline
print = sys.stdout.write


N = int(input())
myQueue = [] # 전용 객체 대신 빈 객체 선언

for _ in range(N):
    request = int(input())

    if request == 0:
        # 리스트가 비어 있다면 0을 출력
        if not myQueue:
            print('0\n')

        else:
            # 큐에서 가장 우선순위가 높은 튜플 빼기
            temp = heapq.heappop(myQueue)
            print(str(temp[1]) + '\n')


    else:
        # 리스트에 데이터 넣기 (넣을 리스트, 넣을 데이터)
        # 절댓값 조건의 튜플 로직 지키기
        heapq.heappush(myQueue, (abs(request),request))
