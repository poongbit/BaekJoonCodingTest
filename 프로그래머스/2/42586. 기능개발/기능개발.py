from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    
    left_work = []
    
    for i in range(len(progresses)):
        days = math.ceil((100-progresses[i])/ speeds[i])
        left_work.append(days)
        
    # ex) [7,3,9]
    q = deque(left_work)
    
    while q:
        
        base = q.popleft()
        
        # popleft 하면서 한 명 나옴
        count = 1
        
        while q and q[0] <= base:
            # base보다 일이 덜 걸려서 이미 일이 끝난 사람들도 같이 걸려서 나옴
            q.popleft()
            count +=1
        
        # 묶인 사람들끼리 나옴
        answer.append(count)
        

    return answer