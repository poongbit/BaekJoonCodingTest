# 최소 신장 트리

"""
최소 신장 트리(크루스칼) 실전 압축 3계명
1.2차원 강박 탈출: 1차원 도로 대장 생성

"노드와 간선이 나왔다!"고 무지성으로 2차원 배열(road_graph[V])부터 파는 습관을 버려야 한다.
크루스칼 알고리즘은 파도타기(탐색)가 아니라 '전국 도로 쇼핑'이다. 
오직 모든 도로의 정보를 담을 1차원 리스트(edges) 딱 하나면 공사 준비가 끝난다!

2. 정렬의 꼼수: 가중치를 맨 앞으로 멱살 잡기

파이썬의 사기 스킬인 sort()는 무조건 튜플의 '첫 번째 원소'를 기준으로 줄을 세운다. 
따라서 제일 싼 도로를 1등으로 뽑아내려면, 리스트에 넣을 때부터 멱살을 잡듯 (비용, 출발지, 도착지) 순서로 비용을 맨 앞에 배치하기!

3. 유니온 파인드 생명줄: return을 잊지 마라

대장을 찾아 거슬러 올라가는 find 함수는 재귀 함수다. 재귀를 돌며 기껏 진짜 대장을 찾아놓고,
 마지막에 return parent[v]로 뱉어내지 않으면 사이클 판독기가 None을 띄우며 장렬하게 폭발한다. 리턴을 절대 빼먹지 말기!

"""




# 문제 1197번 최소 스패닝 트리

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

V,E = map(int,input().split())

parent = [i for i in range(V+1)]
edges = [] # 2차원 배열 대신, 그냥 모든 간선을 담을 1차원 리스트
total_cost = 0 # 최종 아스팔트 공사 비용

# 1. 모든 간선 정보 입력받기
for _ in range(E):
    A,B,C = map(int,input().split())

    # 비용(C)를 맨 앞에 두어, 나중에 sort() 할 때 비용 기준으로 정렬되게 함!
    edges.append((C,A,B))


# 2. 크루스칼의 핵심 : "모든 도로를 싼 순서대로 정렬하라!"
edges.sort()

# 3. 유니온 파인드 함수

def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]


def union(a,b):
    root_a = find(a)
    root_b = find(b)

    if root_a != root_b:
        parent[root_a] = root_b

# 4. 도로 건설 시작
for cost, a,b in edges:
    # 사이클이 발생하지 않는다면 두 도시를 연결한다
    if find(a) != find(b):
        union(a,b)
        total_cost += cost # 공사 비용 추가

print(total_cost)
