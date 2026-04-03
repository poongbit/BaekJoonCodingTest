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
    2. 전력이 소모되는 케이스를 저장해서 각각 꺼낸다.
    3. 조건이 맞는 선에서 전력이 가장 적게 드는 쪽으로 고른다.
    
    """
    
    T = len(onboard) # 시간
    # 최소를 구하는 거니 INF를 설정
    INF = float('inf')
    
    dp = [[INF]*52 for _ in range(T+1)]
    offset = 10 # temp에 들어갈 인덱스가 음수이면 입력이 안됨
    
    # 초기값 설정
    # 현재 0분은 실내온도와 실외온도가 같음, 전력소모 0
    dp[0][offset+temperature] = 0
    
    # 2. 전력이 소모되는 케이스
    
    # t분 동안, 온도의 변화량
    for t in range(T-1):
        for temp in range(-10,41): # 희망 온도 설정중
            
            # 도달하지 못한 곳은 그냥 넘김
            if dp[t][offset+temp] == INF:
                continue
            
            # 도달한 곳에서 (t분일 때 온도 temp)
            cost = dp[t][offset+temp]
            
            candidates = [] # 전이 후보 설정
            
            # 1. 에어컨이 켜져 있을 때
            # 온도를 미리 낮추거나 높힘으로써 조절할 수 있으므로 경우 셋 다 포함
            candidates.append((temp+1,a))
            candidates.append((temp-1,a))
            candidates.append((temp,b))
            
            # 2. 에어컨이 꺼져있을 떄
            if temp > temperature:
                candidates.append((temp-1,0))
                
            elif temp < temperature:
                candidates.append((temp+1,0))
                
            else:
                candidates.append((temp,0))
            
            
            for next_temp, add_cost in candidates:
                
                # 사람이 안 타고 있을 때는 t1,t2 굴레는 없지만, 그래도 최소
                # 온도는 지켜야 함
                if not(-10<=next_temp<=40):
                    continue
                
                # 사람이 탔는데, t1,t2 밖에 있다면 안됨
                if onboard[t+1] == 1 and not(t1<= next_temp <= t2):
                    continue
                    
                idx = next_temp + offset
                    
                dp[t+1][idx] = min(dp[t+1][idx], cost+add_cost) 
                    
    
    
    return min(dp[T-1])
        
    
    
    
    