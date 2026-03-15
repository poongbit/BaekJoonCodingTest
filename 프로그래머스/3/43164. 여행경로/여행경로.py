from collections import defaultdict

def solution(tickets):
    answer = []
    
    # 티켓 사용 여부
    visited = [False] * len(tickets)
    
    
    # 주어진 티켓을 다 활용해야 하고, 다 방문했는 지 체크해야 함
    # 티켓을 다 사용하면 모든 도시를 방문할 수 있음 
    
    def DFS(start,route):
        if len(route) == len(tickets) + 1:
            answer.append(route)
            return
        
        for i in range(len(tickets)):
            # 티켓을 사용하지 않았고, 출발지가 그 티켓의 출발지와 같은 경우
            if not visited[i] and (start == tickets[i][0]):
                visited[i] = True
                DFS(tickets[i][1], route + [tickets[i][1]])
                
                # 다시 돌아올 때 백 트래킹 필요
                visited[i] = False
                
    
    DFS("ICN",["ICN"])
    
    
    return sorted(answer)[0]
    
    
    
    