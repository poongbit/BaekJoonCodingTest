from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    
    # 일이 나가는 순서 - FIFO
    # 배포 타이밍은 앞에 있는 일이 진도율이 꽉 찰 떄 다 같이 나가는 걸로
    
    # 1. 각 progress 마다의 진도율 계산, 배포 되는 타이밍 체크
    left_days = []
    
    for i in range(len(speeds)):
        progress_left = math.ceil((100-progresses[i]) / speeds[i])
        left_days.append(progress_left)
    
    q = deque()
    
    # left days에 큐 집어 넣기
    
    for i in range(len(left_days)):
        q.append(left_days[i])
        
    while q:
        base = q.popleft()
        count = 1
        
        while q and q[0] <= base:
            q.popleft() # base보다 걸리는 작업이 적으면 같이 나감
            count +=1
            
        answer.append(count)
        
        
    
    
    
    
    return answer