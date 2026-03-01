# 문제 25 - 친구 관계 파악하기

"""
N(노드 개수), M(에지 개수)
A (그래프 데이터 저장 인접 리스트)
visited (방문 기록 저장 리스트)
arrive(도착 확인 변수)


# DFS 구현
DFS(현재 노드, 깊이):
    if 깊이가 5:
        arrive = true
        함수 종류

    방문 리스트에 현재 노드 방문 기록
    현재 노드의 연결 노드 중 방문하지 않은 노드로 DFS 실행 # 호출 할 때마다 Depth는 1씩 증가


for M의 개수만큼 반복: # 엣지의 개수만큼
    A 인접 리스트에 그래프 데이터 저장


for N의 개수 만큼 반복:
    노드마다 DFS 실행
    if arrive: 반복문 종료


if arrive: 1 출력
else : 0 출력

"""

import sys
sys.setrecursionlimit(10000)

input = sys.stdin.readline
N,M = map(int,input().split())

arrive = False # depth가 5에 도달하였는 가?
A = [[] for _ in range(N+1)] # 빈 수첩 [ [],[],[],[]...  ] n+1개 생성
visited = [False] * (N+1) # 방문 기록 수첩


def DFS(now,depth):
    global arrive

    if arrive: # 이미 True가 됐으면 바로 끝
        return
    
    if depth == 5:
        arrive = True # 깊이가 5가 되면 종료
        return

    visited[now] = True # now index에는 방문했으니 True

    for i in A[now]:
        if not visited[i]: # 그 친구가 방문이 안됐다면
            DFS(i, depth +1) # 재귀 호출마다 깊이 증가

    visited[now] = False # 뒤로 돌아가서 다른 길을 찾기 위해 길을 지움



for _ in range(M): # 엣지의 개수만큼 노드와 엣지를 받음
    s,e = map(int,input().split())
    A[s].append(e)
    A[e].append(s)



for i in range(N):
    DFS(i,1)
    if arrive:
        break


if arrive:
    print(1)

else:
    print(0)
