def solution(temperature, t1, t2, a, b, onboard):
    
    """
    쾌적 온도 t1~t2 유지 (승객 탑승중일 때)    

    에어컨 on - 희망온도와 같아지는 방향 +-1, 전력 a 소모
            실내오도가 같다면 켜져 있는 동안 온도 안바뀜 - 전력 b 소모
    
    에어컨 off - 실외온도와 같아지는 방향으로 +-1
            실내 온도와  같다면 안 변함 전력 0 소모
            
    
    dp[t][temp] : t분에서 temp 온도 일 때 소모되는 최소 전기량        
    
    """
    
    INF = float('inf')
    T = len(onboard)
    # 인덱스에 영하 10도를 표현할 수 없으므로, offset 착용
    offset = 10
    diverse = 52
    
    # dp 배열 선언
    dp = [[INF] * diverse  for _ in range(T)]
    
    # 0분,기온일 때 전력 소모량
    dp[0][temperature+offset] = 0
    
    # 시간마다, 기온 체크
    
    for time in range(T-1):
        for temp in range(-10,41):
            # 방문하지 않은 시간당 temp는 체크하지 않음
            if dp[time][offset+ temp] == INF:
                continue
            
            # 이 시간 당시의 온도에 따른 전력 소모량 체크
            cost = dp[time][offset + temp]
            
            # 전이 할 수 있는 것들 체크
            check = []
            
            # 1. 에어컨이 꺼저 있을 때
            
            if temp < temperature: # 희망 온도가 외부 온도보다 낮다면:
                check.append((temp + 1,0))
                
            elif temp > temperature: # 희망 온도가 외부 온도보다 높다면:
                check.append((temp-1,0))
                
            else:
                check.append((temp,0))
                
                
            # 2. 에어컨이 켜져 있을 때
            # 에어컨이 켜져 있을 때는 자유롭게 켜고 끌 수 있음
            
            check.append((temp+1,a))
            check.append((temp-1,a))
            check.append((temp,b))
            
            # 각각 꺼내서, 필요한 상황인지 체크
            for next_temp , add_cost in check:
                
                # next_temp가 -10에서 40 사이에 있지 못할 경우
                if not (-10<=next_temp<=40):
                    continue
                
                
                # 다음 승객이 타 있는데 범위 안에 못 들어가면 넘김
                if onboard[time+1] == 1 and not (t1<=next_temp<=t2):
                    continue
                    
                # 다음 온도를 표기하기 위한 인덱스 선언
                idx = next_temp + offset
                
                # 기존에 적힌 비용과 새롭게 계산된 비용과 비교해서 작은 것
                dp[time+1][idx] = min(dp[time+1][idx], cost + add_cost)
                
                
    return min(dp[T-1])
    
    
            
            
            
            
    
    
    
    
    
    