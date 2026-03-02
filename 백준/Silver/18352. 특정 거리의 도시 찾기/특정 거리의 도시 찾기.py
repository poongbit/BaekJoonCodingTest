# BFS 활용하기

"""

DFS : 한 우물만 끝까지 판다 -> 엉뚱한 길로 빙빙 돌아서 잘못된 길로 갈 수 있음
BFS (너비 우선 탐): 호수에 돌맹이를 던진 물결처럼 퍼진다.
공평하게 한 칸씩 넓어지면서, 어떤 방에 도달하는 순간, 그 거리가 무조건 최단 거리임이 보장됨



최단 거리가 정확히 K인 모든 도시들의 번호를 출력하라

N : 노드 개수
M : 에지 개수
K : 목표 거리
X : 시작점

answer = 정답 리스트
visited = 방문 거리 저장 리스트 # -1로 초기화


#BFS 구현하기

BFS:
    큐 자료구조에 시작 노드 삽입
    visited 리스트에 현재 노드 방문 기록 # 거리 저장 형태로 1 증가
    while 큐가 빌 때까지:
        큐에서 노드 데이터 가져오기
        
        if 현재 노드의 연결 노드 중 미방문 노드:
            visited  리스트값 1 증가
            큐에 노드 삽입

    

for M 만큼 반복:
    A 인접 리스트에 그래프 데이터 저장


BFS(X) 실행

for N만큼 반복:
    방문 거리가 K인 노드의 숫자를 정답 리스트에 더하기


정답 리스트 오름차순 정렬 후 순차 출력

"""



import sys
from collections import deque
input = sys.stdin.readline

N,M,K,X = map(int,input().split()) 
A = [[] for _ in range(N+1)]

answer = []
visited = [-1] * (N+1)

def BFS(v):
    queue = deque()
    queue.append(v)

    visited[v] +=1

    while queue:
        now_node = queue.popleft() #선입 선출로 먼저 들어온 놈 나옴 append(오른쪽) -> popleft(왼쪽)
        for i in A[now_node]:
            if visited[i] == -1: #방문 안한 곳이라면
                visited[i] = visited[now_node] + 1
                queue.append(i)


for _ in range(M):
    S,E = map(int,input().split())
    A[S].append(E)


BFS(X)

for i in range(N+1):
    if visited[i] == K:
        answer.append(i)


if not answer:
    print(-1)

else:
    answer.sort()
    for i in answer:
        print(i)
