# 슬라이싱 윈도우
def solution(players, m, k):
    answer = 0
    
    added = [0] * 24
    
    # 0 ~ 23 까지 
    for i in range(24):
        users = players[i]
        need = users // m
        
        # k 시간 전에서부터, i시간까지 살아있는 서버의 수
        current = sum(added[max(0,i-k+1):i+1])
        
        if current < need:
            diff = need - current
            added[i] = diff
            answer += diff
        
    
    
    
    return answer