# FIFO 이므로 , 큐로 구현해야 함
# 컨베이어 벨트식 이동
from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    index = 0 # truck_weights 인덱스를 추적
    current_weight = 0 # 현재 다리에 가해지는 무게
    
    # 컨베이어 벨트 같은 길 초기화
    q = deque([0] * bridge_length)
    # [0,0]
    
    while index < len(truck_weights):
        # 일단 무조건 컨베이어 벨트는 움직여야 함
        removed = q.popleft()
        current_weight -= removed
        answer +=1 # 시간은 1초 흐름
        
        # 1초가 흘렀을 때,
        if current_weight + truck_weights[index] <= weight:
            q.append(truck_weights[index])
            current_weight += truck_weights[index]
            index +=1
            
        else:
            q.append(0)
    
    answer += bridge_length
        
    return answer