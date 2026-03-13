def DFS(n,v,visited,computers):
    
    visited[v] = True
    for i in range(n):
        if computers[v][i] == 1 and not visited[i]:
            DFS(n,i,visited,computers)
            



def solution(n, computers):
    
    answer = 0

    # 1. 입력값 받기, 변수 생성
    
   # DFS를 통해서 연결 상태를 확인한다.
    
    visited = [False] * n
    
    # 모든 노드를 순회해가며 아직 방문 안한 노드 발견할 때마다 새 네트워크임
    
    for i in range(n): 
        if not visited[i]:
            DFS(n,i,visited,computers)
            answer +=1 # 네트워크 하나 발견
    
    
    
    return answer
    
    
                
    
            
            
    
    
    