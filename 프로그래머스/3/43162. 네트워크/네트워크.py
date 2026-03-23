def solution(n, computers):
    
    answer = 0
    
    visited = [False] * n
    
    
    def DFS(v):
        # 노드를 방문함
        visited[v] = True
        
        for i in range(n):
            if computers[v][i] == 1 and not visited[i]:
                DFS(i)
            
    
    for i in range(n):
        if not visited[i]:
            DFS(i)
            answer +=1
            
    
    return answer
    
    
                
    
            
            
    
    
    