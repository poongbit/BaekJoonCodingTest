from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    
    """
    뒤에 있는 기능이 앞에 있는 기능보다 빨리 개발될 수 있음
    
    뒤에 있는 기능은 앞에 있는 기능이 배포될 때, 함께 배포된다 - 큐 활용
    FIFO 스러움
    
    Progresses : 작업의 진도 
    Speed :  개발 속도
    
    """
    
    # 각 작업 완료까지 며칠이 걸리는 가?
    worked_days = []
    
    for i in range(len(progresses)):
        days = math.ceil((100 - progresses[i]) / speeds[i])
        worked_days.append(days)
    
    
    q = deque(worked_days)
    
    while q:
        base = q.popleft()
        count = 1
        
        while q and q[0] <= base: # 다음 값이 기준보다 작으면
            q.popleft() # 같은 묶음으로 처리
            count +=1
            
        answer.append(count)
            
            
    return answer