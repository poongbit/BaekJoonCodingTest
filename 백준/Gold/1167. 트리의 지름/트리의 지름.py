import sys
from collections import deque
input = sys.stdin.readline

# 1. 노드의 개수 N 입력 받기
N = int(input())

# 2. 인접 리스트 생성 (각 노드의 '수첩' 만들기)
A = [[] for _ in range(N+1)]

# 3. 그래프 데이터 이쁘게 저장하기
for _ in range(N):
    data = list(map(int,input().split()))
    node = data[0] # 첫 번째 숫자는 '현재 수첩의 주인(노드)'

    idx = 1

    # -1이 나올 때까지 2개씩(연결되 노드, 거리) 짝지어서 수첩에 적기
    while data[idx] != -1:
        adj_node = data[idx] # 연결된 이웃 노드
        weight = data[idx+1] # 그 이웃까지의 거리 (가중치)

        # 수첩에 (이웃 노드, 거리)를 한 묶음(튜플)로 저장!
        A[node].append((adj_node,weight))
        idx += 2 # 다음 짝을 보기 위해 인덱스를 2칸 점프


# 4. BFS 함수 정의 : (시작점)을 넣으면 -> (가정 먼 노드, 그 거리)를 뱉어낸다.

def BFS(start):
    # 매번 BFS를 돌릴 때마다 방문 기록과 거리 기록을 새것으로 교체(초기화)
    visited = [False] * (N + 1) 
    distance = [0] * (N+1)

    queue = deque()
    queue.append(start)
    visited[start] = True # 시작점 방문 도장 찍기


    #큐가 빌때까지 파문 퍼뜨리기
    while queue:
        now = queue.popleft()

        # 내 수첩(A[now])를 열어서 연결된 이웃들을 하나씩 확인
        for next_node, weight in A[now]:
            if not visited[next_node]: # 아직 안 가본 것이라면?
                visited[next_node] = True # 방문 도장 찍기

                # 다음 칸 바닥에 지금까지 걸어온 거리 + 새로운 길의 거리를 더함

                distance[next_node] = distance[now] + weight

                queue.append(next_node) # 다음 타자 큐에 넣기

    
    # 파문이 다 퍼졌으면, distance 배열에서 가장 거리가 큰 값과 그 노드 번호를 찾기

    max_dist = max(distance)
    farthest_node = distance.index(max_dist)

    return farthest_node, max_dist



# 5. 2-step 탐색 시작

# 1회차 : 아무 노드(1번)에서 냅다 물결을 퍼뜨려서 '메인 고속도로의 한 쪽 끝 점'을 찾는다
far_node, _ = BFS(1)

# 2회차 : 방금 찾은 그 '끝점'에서 다시 물결을 퍼뜨려 반대편 끝점까지의 '최대 길이(지름)'을 잰다!

_,tree_diameter = BFS(far_node)

#결과 출력
print(tree_diameter)