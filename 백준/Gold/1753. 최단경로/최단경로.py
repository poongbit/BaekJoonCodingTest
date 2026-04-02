# 문제 1753 - 최단 경로
import sys
input = sys.stdin.readline

import heapq

V,E = map(int,input().split())

start_node = int(input().strip())

graph = [[] for _ in range(V+1)]

for _ in range(E):
    u,v,e = map(int,input().split())

    graph[u].append((v,e))


INF = float('inf')

# distance에 거리를 저장해두는 배열 생성

distance = [INF] * (V+1)

def BFS(start_node):

    q = []
    # 거리, 스타트 지점을 넣음
    heapq.heappush(q,(0,start_node))

    # 시작 지점은 거리 0으로 초기화
    distance[start_node] = 0

    while q:
        dist, now_node = heapq.heappop(q)

        # 현재 거리가 기록된 거리보다 더 길다면 패스
        if dist > distance[now_node]:
            continue

        
        for next_node, weight in graph[now_node]:
            cost = distance[now_node] + weight

            # 비용이 더 싸다면
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q,(cost,next_node))


BFS(start_node)

for i in range(1,V+1):
    if distance[i] == INF:
        print('INF')

    else:
        print(distance[i])