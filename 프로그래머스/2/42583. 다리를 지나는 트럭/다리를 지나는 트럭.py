from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    # 순서가 중요, FIFO, 큐를 사용하자
    # ex) 트럭이 최대 2대 올라갈 수 있음, 큐가 3개 이상 차면 무조건 내리기
    
    # 다리에 올라갈 수 있는 차의 수
    bridge = [0] * bridge_length
    
    # 큐 선언
    q = deque(bridge)
    
    # 다리를 큐에 넣음 - 컨베이어 벨트처럼 빠져나가게 함
    # append로 하면, 원소로 들어가게 됨
    time = 0
    
    # sum(q)는 O(n) 이므로 O(1)으로 하기 위해
    current_weight = 0
    
    # 다음 트럭 무게 인덱스
    index = 0
    
    while index < len(truck_weights):
        # 컨베이어 벨트 앞으로 나감
        removed = q.popleft()      
        current_weight -= removed
        time +=1
        
        # 남아있는 트럭이 있고, 다리에 있는 무게 합과, 이제 올라갈 트럭의 합이
        # 최대 무게보다 작거나 같다면
        if truck_weights and current_weight + truck_weights[index] <= weight:
            # 대기 트럭을 집어 넣음 (?)
            if truck_weights:
                next_truck = truck_weights[index]
                q.append(next_truck)
                current_weight += next_truck
                index +=1 # 트럭이 다리에 올라탔다는 걸 확인
                
    
        else:
            q.append(0)
    
    time += bridge_length
    
    return time