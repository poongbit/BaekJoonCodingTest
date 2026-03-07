# 문제 1068번

# 1. 입력 받기

import sys
input = sys.stdin.readline
from collections import deque


N = int(input())

# 각 노드들에 대한 부모 노드
parent = list(map(int,input().split()))

node_graph = [[] for _ in range(N)]

# 루트 노드 초기화 
root = 0

for i in range(N):
    
    parent_node = parent[i]

    if parent_node != -1:
        node_graph[parent_node].append(i)

    else:
        root = i
        

deleted_node = int(input())

# 2. BFS 탐색을 통한 리프 노드 탐색

def BFS(root,deleted_node):
    q = deque([root])

    # 뿌리가 사라지면 아래의 노드들은 다 사라지므로, 0
    if root == deleted_node:
        return 0
    
    # 잎 개수 세기 위한 카운팅
    leaf_count = 0

    while q:
        now = q.popleft()

        # 아이 노드 개수 초기화
        child_node = 0

        for next_node in node_graph[now]:
            # 다음 노드가 지워야 할 노드가 아니라면
            if next_node != deleted_node:
                child_node +=1
                q.append(next_node)

        # 자식 노드가 하나도 없다면
        # 내가 그 자식 노드다.
        if child_node == 0:
            leaf_count +=1

    return leaf_count


print(BFS(root,deleted_node))
        
