# 문제 1753 - 최단 경로

"""
다익스트라(Dijkstra) 실전 압축 3계명

1. [무기 장착: 힙 큐와 정렬 기준]

일반 deque 대신 무조건 **heapq**를 쓴다! 가장 짧은(싼) 경로가 1등으로 튀어나와야 하므로, 
큐에 넣을 때는 앞뒤를 뒤집어서 무조건 (거리, 목적지) 순서로 튜플을 묶어 넣는다.

2. [검증: 낡은 티켓은 가차 없이 버려라]

heappop으로 꺼낸 거리(dist)가 이미 내 메모장에 기록된 최솟값(distance[now])보다 크다면? 
이미 더 싼 길을 찾고 지나간 '낡은 정보'이므로 묻지도 따지지도 않고 **continue**로 무시한다!

3. [갱신: 더 싸면 덮어씌우고 큐에 넣어라]

for문을 돌며 이웃 노드로 가는 새로운 비용(cost = dist + weight)을 계산한다. 
만약 이 거쳐가는 비용이 메모장에 적힌 기존 비용보다 싸다면? 과감하게 메모장을 덮어씌우고, 이 싼 경로를 기준으로 다시 파도를 타기 위해 큐에 새롭게 heappush 한다!


"""


import sys
import heapq

input = sys.stdin.readline

# 1. 입력값 받기 및 변수 선언 

V,E = map(int,input().split()) # 정점과 간선
K = int(input()) # 시작 정점 

INF = int(1e9) # 10억

road_graph = [[] for i in range(V+1)] # 경로 데이터 지도

# 시작 정점으로부터 목적지까지의 최소 거리를 담는 공간
distance = [INF] * (V+1)


for _ in range(E):
    s,e,w = map(int,input().split())

    # 간선 데이터 입력 받기

    # 시작점 -> (목적지,간선)
    road_graph[s].append((e,w)) 


# 2. 다익스트라 함수 선언

def dijkstra(start):
    q = [] # 힙 큐라서 일반 배열 선언

    # 초기 시작 노드 설정

    # heap은 첫 번째를 기준으로 정렬하므로
    # 순서를 반대로 집어넣어줌 (w,e)
    heapq.heappush(q,(0,start))

    distance[start] = 0

    while q:
        dist, now_node = heapq.heappop(q)

        # 이미 처리된 적이 있는 노드라면, 지나감
        if dist > distance[now_node]:
            continue
        

        for next_node, weight in road_graph[now_node]:
            cost = distance[now_node] + weight

            # 현재 노드를 거쳐 가는게, 정점에서 next_node로 가는 것 보다 빠르다면
            if cost < distance[next_node]:
                distance[next_node]  = cost

                # next_node를 거쳐 가므로,
                # 이 싼 경로를 기준으로 그 다음 노드를 큐에 넣음
                heapq.heappush(q,(cost,next_node))



dijkstra(K)


for i in range(1,V+1):
    if distance[i] == INF:
        print("INF")

    else:
        print(distance[i])
