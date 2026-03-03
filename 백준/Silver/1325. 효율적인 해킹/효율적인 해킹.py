# 문제 50 - 효울적으로 해킹하기 1325번


from collections import deque
import sys

input = sys.stdin.readline

N,M = map(int,input().split())

A = [[] for _ in range(N+1)] # 노드 개수만큼 인접 리스트 생성

# 1. 데이터 입력받기

for _ in range(M):
    s,e = map(int,input().split())

    A[e].append(s) # B를 해킹하면 A를 해킹하므로 단방향임

# 2. BFS 설계하기

def BFS(v): # v: 노드
    queue = deque() # 빈 큐 생성
    queue.append(v) # 빈 큐 안에 노드 v append
    

    visited = [False] * (N+1) # 각각 BFS를 돌 때마다 새 출석부를 부름
    visited[v] = True # 방문은 했으니 True로 도장 찍기
    count = 1 # v 노드를 방문했으므로, 감염 횟수는 1부터 시작

    while queue: # 큐 안에 노드가 있는 동안
        now_node = queue.popleft() # 가장 먼저 들어온 노드를 반환함

        for next_node in A[now_node]: # now node 안에 있는 다음 리스트들에 대해서
            if not visited[next_node]: # 방문한 적이 없다면
                visited[next_node] = True # 방문한 기록 체크
                count += 1 # 감염 횟수 1회 증가
                queue.append(next_node) # 큐에 다음 노드를 삽입하기
    
    return count


# 3. 각각 BFS를 실행시켜서 가장 감염을 많이 시킨 노드를 기록하기

answer = [] # 가장 많이 감염시킨 노드 기록

max_count = 0 # 가장 감염 많이 시킨 횟수


for i in range(1,N+1): # 1번 노드부터 N번 노드까지 BFS 작동
    temp = BFS(i)

    if temp > max_count:
        answer = [i] # 가장 많은 감염시킨 노드 '하나'로 기록
        max_count = temp

    elif temp == max_count: # 동점인 경우:
        answer.append(i) # 동점인 노드를 추가해서 기록

for i in answer:
    print(i,end = " ")