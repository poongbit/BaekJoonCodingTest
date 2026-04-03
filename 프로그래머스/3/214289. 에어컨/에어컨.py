def solution(temperature, t1, t2, a, b, onboard):
    
    """
    실내온도 t1,t2 - 승객 탑승 중일 때
    
    희망온도 - 전원 켜져있는 동안 원하는 값으로 변경 가능
    
    에어컨 on -> 실내온도 != 희망온도 -> 희망온도로 +-1 / 전력 a 소비
                같으면 변화x / 전력 소모 b
                
    에어컨 off -> 실내온도 -> 실외온도와 같아지는 방향 +-1 / 전력 0 소모
                같으면 변화 x
    
    켜고 끄는데 전력 소모 0 가정
    
    목표 : 승객 탑승 중일 때 t1~t2 유지 + 에어컨 소비전력 최소화
                
    
    실외온도 = temperature
    실내 온도 범위 t1,t2
    에어컨 소비 전력 a,b
    승객이 탑승중인 시간 1차원 정수 배열 onboard
    
    탑승중인 시간에 쾌적한 실내온도 유지를 위한 최소 소비 전력?
    
    """
    
    # DFS BFS 하기에는 조건에 따라서 전력 소모가 왔다 갔다 함
    # 아예 값 자체를 저장 다 해버리는 걸로 해볼까? DP로
    
    # dp[i][temp] = i분 때에 temp 온도일 떄 소모되는 최소 전력
    
    """
    1. dp 배열 선언
    dp[t][temp] = t분 때에 temp 온도일 때 소모되는 최소 전력
    2. 전력이 소모되는 케이스를 candidates[] 리스트에 담아 넣는다
    
    for t in range(T-1):
        for temp in range(-10,41):
        
        t분일 때 온도를 기준으로 전이 상태를 가져온다.
    
    
    3. 조건이 맞는 선에서 dp를 최소값을 구한다.
    
    """
    
    T = len(onboard)
    
    # 최소를 구해야 하기 때문에 INF
    INF = float('inf')
    # 온도 variation이 52임
    dp = [[INF] * 52 for _ in range(T+1)]
    
    offset = 10 # 온도에 영하도 들어갈 수 있음
    
    # 0분일 때 실내온도는 실외 온도와 같다., 그 때의 전력 소모량
    dp[0][temperature + offset] = 0
    
    for t in range(T-1):
        for temp in range(-10,41): # 희망 온도 설정
            # 초반에 0분일 때 INF인 경우는 넘기기
            if dp[t][temp+offset] == INF:
                continue
            
            # 비용 선언, 나중에 변화하면서 더해지는 거 생각
            cost = dp[t][temp+offset]
            
            # t,temp에 따른 전이 상태를 저장한다
            candidates = []
            
            # 1. 에어컨이 켜진 경우
            # 선택지를 이런식으로 골라볼 수 있음
            candidates.append((temp+1,a))
            candidates.append((temp-1,a)) # 온도가 다른 경우
            candidates.append((temp,b)) # 온도가 같은 경우
            
            # 2. 에어컨이 꺼져있을 경우
            
            if temp > temperature:
                candidates.append((temp-1,0))
                
            elif temp < temperature:
                candidates.append((temp+1,0))
                
            else:
                candidates.append((temp,0))
                
            # 시간과 온도가 딱 정해진 후,
            
            for next_temp, add_cost in candidates:
                # 존재할 수 있는 기온을 넘어선 경우
                if not (-10<=next_temp<=40):
                    continue # 넘김
                
                # 다음에 사람이 탈 것으로 예상되는데,
                # 온도가 기준에 못 맞을 경우 넘김 
                if onboard[t+1] == 1 and not(t1<=next_temp<=t2):
                    continue
                    
                # 기온이 영하가 되는 경우도 있으므로, 인덱스 변수 따로 선언
                idx = next_temp + offset
                
                # 그 다음 최소 전력은, 기존에 저장된거랑, 루프하면서 저장된 것중
                # 작은걸로 업데이트 한다.
                dp[t+1][idx] = min(dp[t+1][idx], cost + add_cost)
            
    
    
    return min(dp[T-1])
            
            
    
    
    
    
    