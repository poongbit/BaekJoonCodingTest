from collections import deque

import sys
input = sys.stdin.readline

graph = []

N = int(input().strip())

node = int(input().strip())

graph = [[]*(N+1) for _ in range(N+1)]

for _ in range(node):
    s,e = map(int,input().split())

    graph[s].append(e)
    graph[e].append(s)


visited = [False] * (N+1)

def BFS(node):
    q = deque([node])

    visited[node] = True

    count = 0

    while q:
        now_node = q.popleft()

        for next_node in graph[now_node]:
            if not visited[next_node]:
                count +=1
                visited[next_node] = True
                q.append(next_node)
    
    return count


answer = BFS(1)

print(answer)