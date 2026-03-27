import math
def solution(n, wires):
    answer = n
    
    def DFS(v,graph):
        # 송전탑 방문 성공
        visited[v] = True
        count = 1
        
        for next_node in graph[v]:
            if not visited[next_node]:
                count += DFS(next_node,graph) # 누적
                

        return count
    
    
    # i번쨰 wire를 끊어버린다는 가정 하에
    for i in range(len(wires)):
        w_graph = [[] for _ in range(n+1)]
        
        for j,(v1,v2) in enumerate(wires):
            # i번째 전력망이면 그냥 데이터 안 넣고 넘어감
            if i == j:
                continue
            w_graph[v1].append(v2)
            w_graph[v2].append(v1)
            
        # 송전탑 방문 기록 선언하기
        visited = [False] * (n+1)
        
        # 횟수 세기
        count = 0
        
        result = DFS(1,w_graph)
        
        other_side = n - result
        
        diff = abs(result - other_side)
        
        answer = min(diff,answer)
            
        
    
    return answer