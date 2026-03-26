from collections import deque

def solution(n, infection, edges, k):
    answer = 0

    # 1. 양방향 그래프 생성
    virus_graph = [[] for _ in range(n+1)]
    
    for x,y,p_type in edges:
        virus_graph[x].append((y,p_type))
        virus_graph[y].append((x,p_type))
    
    # 2. spread 함수- BFS로 감염 전파
    
    def spread(infected_set,p_type):
        # 새로운 new_infected
        
        # 새로운 거는 기존에 것과 추가할 수 있도록 복사해둠
        new_infected = set(infected_set)
        
        q = deque(infected_set)
        
        while q:
            now_node = q.popleft()
            for next_node, next_type in virus_graph[now_node]:
                # 다음 타입이 spread할 타입과 같고, new_infected에 없는 새 노드
                if next_type == p_type and next_node not in new_infected:
                    new_infected.add(next_node)
                    q.append(next_node)
        
        return new_infected
    
    answer = [0]
    
    # 3. dfs 함수 호출 - > 타입 순열 검색
    def DFS(remaining, infected_set, prev_type):
        answer[0] = max(answer[0],len(infected_set))
        # 반복이 다 끝났으면 종료
        if remaining == 0:
            return 
        
        # 타입 1,2,3
        for p_type in [1,2,3]:
            if p_type == prev_type:
                continue
            new_infected = spread(infected_set,p_type)
            DFS(remaining-1,new_infected,p_type)    
    
    
    # 4. dfs 호출 - 리턴
        
    DFS(k,{infection},None)
    
    
    return answer[0]