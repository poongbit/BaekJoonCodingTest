# 문제 29. DFS와 BFS 프로그램 1260번

"""
N : 노드의 개수 
M : 엣지의 개수
start : 시작점

A : 그래프 데이터 저장 인접 리스트

for M의 개수 만큼 반복:
    A 인접 리스트에 그래프 데이터 저장


# 방문할 수 있는 노드가 여러개 일 때, 번호가 작은 것 부터 먼저 방문하기 위해 정렬

for N+1의 개수만큼 반복:
    각 노드와 관련된 에지를 정렬



# DFS 구현하기
DFS:
    현재 노드 출력하기
    visited 리스트에 현재 노드 방문 기록
    현재 노드의 연결 노드 중 방문하지 않은 노드로 DFS 실행하기 (재귀 함수 형태)


# BFS 구현하기
BFS:
    큐 자료구조에 시작 노드 삽입
    visited 리스트에 현재 노드 방문 기록
    while 큐가 빌 때까지:
        큐에서 노드 데이터를 가져오기
        가져온 노드 출력
        현재 노드의 연결 노드 중 미방문 노드를 큐에 삽입(append 연산)하고 방문 리스트에 기록


visited 리스트 초기화
BFS(start) 실행

"""



from collections import deque
import sys

input = sys.stdin.readline

N,M,start = map(int,input().split())

A = [[] for _ in range(N+1)] # 인접 리스트 생성

for _ in range(M): # 엣지의 개수만큼 반복
    s,e = map(int,input().split())

    # 양방향 엣지이므로 양쪽에 엣지를 더함
    A[s].append(e)
    A[e].append(s)

for i in range(N+1):
    A[i].sort() # 번호가 작은 노드부터 방문하기 위해 정렬하기

def DFS(v):
    print(v,end= ' ')
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            DFS(i)


visited = [False] * (N+1)
DFS(start)


def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        now_Node = queue.popleft() # 지금 노드는 pop시킴
        print(now_Node, end = ' ')
        for i in A[now_Node]: # now_Node안에 있는 노드에서
            if not visited[i]: # 방문 안한 것이 있다면
                visited[i] = True # 방문했다는 표시 체크하고
                queue.append(i) # 큐에 추가함

print()
visited = [False] * (N+1)
BFS(start)
