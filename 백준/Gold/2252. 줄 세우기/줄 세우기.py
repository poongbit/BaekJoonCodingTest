"""
1. [명분] indegree(진입 차수)를 활용해서 A-B 선후 관계의 순서를 명확하게 구분할 수 있다.
2. [시작] BFS 형태를 띠며, 출발 전에 반드시 진입 차수가 0인(조건이 없는) 초기 지점들을 모두 찾아 큐에 선언해야 한다.
3. [엔진] 큐에서 원소를 꺼낼 때마다 다음 타자의 진입 차수를 1씩 깎고, 0이 되는 순간 큐에 삽입하는 '연쇄 해금' 작용을 일으킨다!

"""

import sys
input = sys.stdin.readline
from collections import deque

N,M = map(int,input().split())

# 학생들 간의 키 우열 넣기 위한 정보
indegree = [0] * (N+1)
graph = [[] for _ in range(N+1)]


# 간선 정보 입력 받기
for _ in range(M):
    a,b = map(int,input().split())

    graph[a].append(b) # A가 나와야 B가 나올 수 있음
    indegree[b] += 1 # B가 나오기 위해 선행되어야 할 것들


# topology() 정렬

def topology():

    # 결과를 저장할 배열 선언
    result = []

    # 큐 스택 선언
    q = deque()

    # 초기 지점 선언
    for i in range(1,N+1):
        if indegree[i] == 0:
            q.append(i) # 선행될 것들이 없다면 그 노드를 큐에 넣음


    while q:
        now_node = q.popleft() # 큐에서 현재 노드를 꺼냄

        result.append(now_node) # indegree가 0이므로, 그 결괏값을 result에 append한다.

        indegree[now_node] -=1 # 현재 노드를 꺼냈으므로 카운트 하나 빠짐

        for next_node in graph[now_node]: # 현재 노드 안에 다음 노드들
            indegree[next_node] -=1 # 다음 노드를 꺼냇으므로 카운트 -1

            if indegree[next_node] == 0: # 이후에 선행되어야 할 것들이 없다면
                q.append(next_node) # 다음 노드는 큐에 넣는다.


    for i in result:
        print(i, end= " ")


topology()
