from collections import defaultdict

def solution(tickets):
    answer = []
    
    # 모든 경로를 방문해야 하므로, DFS
    # 티켓을 쓴 것 여부를 기록
    visited = [False] * len(tickets)
    
    
    def DFS(start,current):
        # current에 전 도시를 다 둘러봤다면
        if len(current) == len(tickets) + 1:
            # current를 answer에 합치기
            answer.append(current)
    
        for i in range(len(tickets)):
            # 티켓의 출발 지점과 초기 지점이 같고, 그 티켓을 쓰지 않았다면,
            if tickets[i][0] == start and not visited[i]:
                visited[i] = True
                # 도착지, current + 도착지
                DFS(tickets[i][1], current + [tickets[i][1]])
                visited[i] = False
    
    
    DFS("ICN",['ICN'])
    
    answer.sort()
    
    
    return answer[0]
    
    
    