from collections import deque
def solution(n, infection, edges, k):
    answer = 0
    
    # 바이러스 노드들과 엣지들간의 연결을 담은 전체 맵
    infected_graph = [[] for _ in range(n+1)]
    
    # 양방향 그래프임 - 둘 다 연결되어 있으므로
    for x,y,p_type in edges:
        infected_graph[x].append((y,p_type))
        infected_graph[y].append((x,p_type))
    
    # 감염된 노드, 중복되는 건 자동으로 처리해줌
    infected = set()
    
    # 2. 감염되었을 떄 전파되는 것, BFS
    def spread(infected_set,pipe_type):
        # infected_set : 현재 감염된 노드들
        # pipe_type : 이번에 열 파이프 타입
        new_infected = set(infected_set) # 복사 (원본 유지)
        queue = deque(infected_set)
        
        while queue:
            node = queue.popleft()
            for next_node, t in infected_graph[node]:
                if t == pipe_type and next_node not in new_infected:
                    new_infected.add(next_node)
                    queue.append(next_node)
                    
                    
        return new_infected
    
    
    # 3. 순열 탐색
    answer = [0]
    
    def dfs(remaining,infected_set, prev_type):
        answer[0] = max(answer[0],len(infected_set))
        
        if remaining == 0:
            return
        
        for pipe_type in [1,2,3]:
            if pipe_type == prev_type: # 연속 같은 타입은 스킵
                continue
                
            new_infected = spread(infected_set,pipe_type)
            dfs(remaining-1, new_infected,pipe_type)
    
    
    dfs(k,{infection},None)
    return answer[0]
        
    