def solution(n, computers):
    
    answer = 0
    
    # 방문 도장 생성
    visited = [False] * n
    
    def DFS(v):
        # 방문 도장 쾅 찍기
        visited[v] = True
        
        for i in range(n): # 모든 노드를 훑으면서
            if computers[v][i] == 1 and not visited[i]:
                visited[i] = True
                DFS(i)
        
    for i in range(n): # 0-based index
        if not visited[i]:
            DFS(i)
            answer +=1
    
    
    return answer
    
    
                
    
            
            
    
    
    