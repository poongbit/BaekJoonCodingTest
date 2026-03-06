# 문제 1916 - 최소 비용 구하기
"""
다익스트라 실전 압축 3계명: 최단 경로의 본질

1. 1차원 배열의 마법: 한 놈만 팬다

 다익스트라는 특정 '시작점 하나'에서 다른 모든 도시로 퍼져나가는 단일 출발지 알고리즘이다.
 따라서 목적지가 따로 주어지더라도 복잡한 2차원 배열(cost[출발][도착])은 버리고,
 오직 1차원 배열(cost[N+1]) 하나에 모든 최단 거리를 갱신해 나간다.


2. 첫 단추 초기화: 내 집 앞은 0보
내 위치에서 내 위치로 가는 비용은 당연히 0원이다. 알고리즘의 진짜 시작은 목적지에 값을 넣는 것이 아니라,
 출발지 자신의 비용을 0으로 세팅(cost[start] = 0)하여 파도타기의 진원지를 만드는 것

3. 무한대(INF) 방패
계속해서 더 싼 값으로 덮어씌우는(min) 갱신 로직을 써야 하므로, 
초기 거리는 절대 도달할 수 없는 넉넉한 최댓값인 INF = int(1e9) (10억)으로 세팅하여 예기치 못한 비용 초과 에러를 완벽히 차단!

"""


import sys
import heapq
input = sys.stdin.readline

# 1. 입력값 받기

N = int(input()) # 도시의 개수
M = int(input()) # 버스의 개수

INF = int(1e9)

cost = [INF] * (N+1) # 정점에서 출발해서 도착할 때까지의 버스 비용

# 버스 정보 데이터
bus_graph = [[] for i in range((N+1))]


# 버스 정보 입력 받기
for _ in range(M):
    s,e,w = map(int,input().split())
    bus_graph[s].append((e,w))

# 구간 출발점, 도착점 입력 받기
start,end = map(int,input().split())



# 2. 다익스트라 함수 선언

def dijkstra(K,target): # K : 시작점, target : 목적지
    
    # heap큐를 쓰기 위해 빈 배열 선언
    q = []
    
    # 시작점 K에서 출발하기
    # 처음 출발할 때는 버스 비용이 0
    heapq.heappush(q,(0,K))
    cost[K] = 0 


    while q:
        bus_cost, now_node = heapq.heappop(q)

        # 종착지에 도착하면 break
        if now_node == target:
            break

        # 이미 한번 비용이 갱신 된 경우
        if cost[now_node] < bus_cost:
            continue
        

        for next_node, weight in bus_graph[now_node]:
            next_bus_cost = bus_cost + weight

            if next_bus_cost < cost[next_node]:
                cost[next_node] = next_bus_cost

                # 갱신된 버스 비용과 다음 노드를 큐에 넣어준다
                heapq.heappush(q,(next_bus_cost,next_node))


dijkstra(start,end)


print(cost[end])