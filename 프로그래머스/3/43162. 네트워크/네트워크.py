def solution(n, computers):
    
    answer = 0
    
    visited = [False] * n
    
    def DFS(node):
        # 노드 방문 완료
        visited[node] = True 
        
        for i in range(n):
            # i 노드에 방문을 하지 않았고, node와 i가 연결되어 있다면
            if not visited[i] and computers[node][i] == 1: 
                visited[i] = True
                DFS(i)
    
    for i in range(n):
        if not visited[i]:
            DFS(i)
            answer +=1
    
    
    
    return answer
    
    
                
    
            
            
    
    
    