# 문제 51 - 이분 그래프 판별하기 -1707번


#  핵심 무기: visited를 [0, 1, -1]로 설정하고, 다음 노드에 (현재 노드 * -1)을 곱해 색칠 놀이!
#  간선 주의: 팀을 나누는 것이므로 무조건 '양방향(A[s].append(e), A[e].append(s))' 연결!
#  쪼개진 섬 주의: 출석부(visited)는 탐색 전 딱 1번만 초기화하고, for문으로 1~V번까지 싹 다 찔러볼 것!

"""
if 1) 문제에 모든 정점이 연결되어 있다는 말이 없다면? (또는 섬, 네트워크 묶음을 구하라 하면?)

무조건 for i in range(1,V+1):
    if visited[i] == 0:
        BFS(i) 

BFS(i) 템플릿을 꺼낸다! (단일 BFS 호출 절대 금지)


if 2) 이분 그래프, 두 그룹으로 나누기, 적과 아군 같은 키워드가 나오면?
출석부를 visited = [0] 으로 만들고 -1,1을 곱해가며 색칠놀이 한다.

"""



import sys
from collections import deque

input = sys.stdin.readline


# BFS 구현하기

def BFS(v):
    queue = deque()
    queue.append(v)

    # 1. 디폴트는 빨간색으로 먼저 시작 -1

    visited[v] = -1

    while queue:
        now_node = queue.popleft() # 현재 노드 꺼내기

        for next_node in A[now_node]: # now 노드에 있는 다음 노드들 꺼내기
            if visited[next_node] == 0: # 아직 색칠이 안 칠해진 경우
                visited[next_node] = visited[now_node] * -1 # 일단 현재 노드랑 무조건 반대 색으로!
                queue.append(next_node) # 그리고 다음 노드 탐색 추가하기
            
            elif visited[next_node] == visited[now_node]: # 다음 노드가 현재 노드와 같은 경우
                return False # 이분 그래프 못하므로 False 반환
                break

            # 현재 노드와 다음 노드가 색이 다른 경우, 이미 잘 구분됐으므로 넘어감


    return True 



# 테스트 케이스 입력받기

K = int(input())

for _ in range(K):
    V,E = map(int,input().split())

    A = [[] for _ in range(V+1)] # 인접 리스트 생성

    for _ in range(E): #엣지 데이터 입력받기
        s,e = map(int,input().split())

        # 양방향 노드로 연결
        A[s].append(e)
        A[e].append(s)

    visited = [0] * (V+1) # 이분 그래프로 나누기 위해, 빨간색 -1, 파란색 +1, 안 칠함 0 으로 구분

    is_bipartie = True # 이분 그래프인지 여부 체크 , 디폴트는 True

    for i in range(1,V+1):

        # 이 조건이 없으면, 이미 색칠한 공간에 또 색을 칠하게 되버리므로 조심!
        if visited[i] == 0: # 아직 한번도 안 칠한 부분에서만 체크하기
            temp = BFS(i)

            if temp == False:
                is_bipartie = False
                break

    if is_bipartie:
        print("YES")

    else:
        print("NO")

