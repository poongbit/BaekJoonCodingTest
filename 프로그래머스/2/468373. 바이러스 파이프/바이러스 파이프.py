from collections import deque
import math
def solution(n, infection, edges, k):
    answer = [0] * n
    
    # 1. 양방향 그래프 구성
    infected_graph = [[] for _ in range(n+1)]
    
    for x,y,p_type in edges:
        infected_graph[x].append((y,p_type))
        infected_graph[y].append((x,p_type))
    
    
    # 2. spread 함수 - BFS로 타입 열면 감염 전파
    
    def spread(infected_group,pipe_type):
        q = deque(infected_group)
        
        new_infected = set(infected_group)
        
        while q:
            now_node = q.popleft()
            
            for next_node,p_type in infected_graph[now_node]:
                if next_node not in new_infected and p_type == pipe_type:
                    new_infected.add(next_node)
                    q.append(next_node)
                    
        return new_infected
        
    
    
    
    # 3. DFS 함수 - 타입 선택 순서 완전탐색
    def DFS(remaining,infected,pipe_type):
        answer[0] = max(answer[0],len(infected))
        if remaining == 0:
            return
        
        for item in [1,2,3]:
            if item == pipe_type:
                continue
                
            new_infected = spread(infected,item)
            
            DFS(remaining-1,new_infected,item)    
    
    
    # 4. DFS 실행 + return
    DFS(k,{infection},None)    
    
    
    return answer[0]