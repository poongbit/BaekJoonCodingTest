def solution(temperature, t1, t2, a, b, onboard):
    INF = float('inf')
    T = len(onboard)
    # 영하 10도도 있으므로, 상쇄시킬 수 있어야 함 
    offset = 10
    SIZE = 51 # -10 ~ 40
    
    dp = [[INF] * SIZE for _ in range(T)]
    dp[0][temperature + offset] = 0
    
    for t in range(T-1):
        for temp in range(-10,41):
            if dp[t][temp + offset] == INF:
                continue
            
            # t분 후의 온도에 대한 비용을 기록
            cost = dp[t][temp + offset]
            
            # 전이 후보 (next_temp,추가 비용)
            candidates = []
            
            # 1. 에어컨 off -> 실외 온도 방향으로 1도
            
            if temperature > temp:
                candidates.append((temp+1,0))
                
            elif temperature < temp:
                candidates.append((temp-1,0))
                
            else:
                candidates.append((temp,0))
            
            # 2. 에어컨 ON, 현재 온도 유지 (희망 온도 = temp)
            candidates.append((temp,b))
            
            # 3. 에어컨 ON, 1도 올리기 (희망온도 > temp)
            candidates.append((temp+1,a))
            
            # 4. 에어컨 ON, 1도 내리기 (희망온도 < temp)
            candidates.append((temp-1,a))
            
            
            for next_temp, add_cost in candidates:
                # 온도 범위 체크
                if not (-10<=next_temp<=40):
                    continue
                    
                # 승객 탑승 중이면 쾌적 온도 범위 체크
                if onboard[t+1] == 1:
                    if not (t1 <= next_temp <=t2):
                        continue
                        
                idx = next_temp + offset
                # 여러가지 경로 중 가장 싼 것만 살아남은 경로
                dp[t+1][idx] = min(dp[t+1][idx],cost + add_cost)
                
                
        # 마지막 분에서 최솟값
    
    return min(dp[T-1])
                    
            
            
            
            
            
            