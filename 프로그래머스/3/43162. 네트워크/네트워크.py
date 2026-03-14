def solution(n, computers):
    
    answer = 0

    visited = [False] * n

    
    def DFS(v):
        visited[v] = True
                    
        for i in range(n):
            if not visited[i]:
                if computers[v][i] == 1:
                    DFS(i)
                    
    
    for i in range(n):
        if not visited[i]:
            DFS(i)
            answer +=1
    
    
        

    return answer
    
    
                
    
            
            
    
    
    