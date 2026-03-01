# 문제 23. 연결요소 개수 구하기 - 11724번

"""

n: 노드의 개수, m: 에지 개수

A: 그래프 데이터 저장 인접 리스트
visited : 방문 기록 리스트


# DFS 구현

DFS:
    visited 리스트에 현재 노드 방문 기록
    현재 노드의 연결 노드 중 방문하지 않은 노드로 DFS 실행 (재귀 함수 형태)

for m의 개수만큼 반복:
    A 인접 리스트에 그래프 데이터 저장

for n의 개수 만큼 반복:
    if 방문하지 않은 노드가 있다면:
        연결 요소 개수 값 1 증가
        DFS 실행

"""

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000) # 재귀 반복 횟수를 10000번까지 풀어준다.

n,m = map(int,input().split())
A = [[] for _ in range(n+1)] # [ [], [], [], ...] 텅 빈 리스트(수첩)을 N+1개를 만든다.
# 1번 학생의 친구 목록 적을 빈칸, .... 같은 비상 연락망
# 0번방부터 n번방까지, 0번 방은 안씀

visited = [False] * (n+1) # 방문 체크를 담은 리스트
# 0번방부터 n번방까지, 0번방은 안씀


# 1. 비상 연락망 만들기
for _ in range(m):
    s,e = map(int, input().split())

    # 양방향 엣지이므로 양쪽에 엣지를 더하기
    A[s].append(e) # s의 수첩에 e를 적는다.
    A[e].append(s) # e의 수첩에 s를 적는다. (서로 아는 사이이기 때문!
    
# A 수첩에는 각 사람마다 누구랑 친한 지 번호가 다 적히게 됨


# 2. 미친듯한 꼬리 물기
def DFS(v):
    visited[v] = True # 여기 방문했다.

    for i in A[v]: # 내 수첩(A[v]) 에서 친구들(i)을 한 명씩 부름
        if not visited[i]: # i 친구가 방문을 안했다고 했을 때
            DFS(i) # 그 친구한테 쳐들어가서 똑같은 짓을 시킴 (재귀)


count = 0

for i in range(1,n+1): # 1번부터 n번 학생까지 다 부름
    if not visited[i]: # i번 학생이, 방문 안한게 탈로 나면
        count +=1 # 새로운 단톡방을 탄다.
        DFS(i) #관련된 애들 싹 다 서려와서 체크


print(count)


