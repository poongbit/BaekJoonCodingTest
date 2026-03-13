from collections import deque


def BFS(n,v,graph):
    
    # 큐 스택 초기화
    q = deque()
    
    # 출석부 작성
    visited = [False] * (n+1)
    
    visited[v] = True
    
    # 초기 스택에 들어감
    q.append(v)
    
    size = 1
    
    while q:
        now_node = q.popleft()
        
        for next_node in graph[now_node]:
            if visited[next_node] != True:
                visited[next_node] = True
                size +=1
                q.append(next_node)
                
    return size
        



def solution(n, wires):
    answer = n
    
    
    for i in range(len(wires)):
        # i 번쨰 간선만 제외하고 그래프 구성
        tree_graph = [[] * (n+1) for _ in range(n+1)]
        
        for j in range(len(wires)):
            if i == j:
                continue
                
            else:
                a,b = wires[j][0], wires[j][1]
                
                tree_graph[a].append(b)
                tree_graph[b].append(a)
    
       
        new_size = BFS(n,1,tree_graph)
        diff = abs(new_size - (n - new_size))
                
        if diff < answer:
            answer = diff
        
    
    return answer