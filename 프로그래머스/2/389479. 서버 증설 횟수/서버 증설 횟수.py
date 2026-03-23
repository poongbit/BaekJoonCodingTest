# 슬라이싱 윈도우
def solution(players, m, k):
    answer = 0
    
    # 0~23시까지 서버가 작동하는 것을 기록
    added = [0] * len(players)
    
    count = 0
    # i시간 동안 일어나는 일
    for i in range(24):
        users = players[i]
        
        # 이 시간대에 필요한 추가 서버 수
        needed = users // m
        
        # 현재 작동 중인 서버 수
        now_worked = added[max(0,i-k+1):i+1]
        
        if needed > sum(now_worked):
            diff = needed - sum(now_worked)
            added[i] += diff
            answer += diff
        
    
    
    return answer