from collections import defaultdict

def solution(tickets):
    answer = []

    airport_graph = defaultdict(list)
    
    # 티켓 번호에 대응된다.
    visited = [False] * len(tickets)
    
    # 1. 입력값 입력 받기
    for a,b in tickets:
        airport_graph[a].append(b)
    
    
    def DFS(current,route):
        # 1. 종료 조건
        # 티켓은 3장, 경로는 4장
        if len(route) == len(tickets) + 1:
            answer.append(route)
            return
        
        # 2. 티켓 순회
        
        for i in range(len(tickets)):
            if not visited[i] and tickets[i][0] == current:
                
                # 3. 방문 처리 + 재귀 + 백트래킹
                visited[i] = True
                DFS(tickets[i][1], route + [tickets[i][1]])
                visited[i] = False
        
    DFS("ICN",["ICN"]) # 항상 ICN 출발, 경로에 ICN 포함
    
    
    return sorted(answer)[0] # 알파벳 순서 앞서는 기준으로