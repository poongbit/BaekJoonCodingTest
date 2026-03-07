import sys
input = sys.stdin.readline
from collections import deque

"""
트리의 부모 찾기 (백준 11725)
1. 입력의 함정 회피: 무조건 양방향 도로 뚫기

출제자는 "누가 부모고 자식인지" 절대 친절하게 알려주지 않는다!
간선 정보가 들어오면 무지성으로 tree[s].append(e)와 tree[e].append(s)를 둘 다 작성하여,
일단 양방향으로 길을 모두 열어두는 것이 트리의 첫 단추다.

2. 탐색의 무기: 루트에서 시작하는 BFS 파도타기

트리는 사이클이 없는 위에서 아래로 흐르는 물과 같다! 문제에서 꼭대기(루트 1번)를 알려줬으니, 큐(deque)에 1번을 넣고 
BFS를 돌리며 물을 아래로 쫙 흘려보내면 순회가 끝난다.

3.  1차원 부모 기록장

방문 도장(visited)과 정답 배열을 따로 만들 필요가 없다!
parent = [0] * (N+1) 배열을 만들고, 이웃의 값이 0이라면 "어? 아직 방문 안 한 내 자식이네?" 하고 내 번호를 적어주면 끝난다. 
방문 체크와 부모 기록을 한 방에 해결!



"""

root = 1

# 입력 받기

# 노드의 개수

N = int(input())

tree = [[] for _ in range(N+1)]
parent = [0] * (N+1) # 부모 노드를 기록할 공간


for _ in range(N-1):
    s,e = map(int,input().split())

    # 둘 중 누가 부모이고 자식인지는 안 알려줌
    tree[s].append(e) # s의 자식은 e
    tree[e].append(s) # e의 자식은 s



def search_tree():
    # q 배열 선언(루트 노드가 1임을 이미 암)
    q = deque([1])

    while q:
        now = q.popleft()

        for next_node in tree[now]:
            # 부모 노드가 아직 기록이 안됐다면
            if parent[next_node] == 0:
                parent[next_node] = now

                # 파도 타기는 계속
                q.append(next_node)

search_tree()

for i in range(2,N+1):
    print(parent[i])