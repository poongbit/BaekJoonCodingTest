from collections import deque

def solution(priorities, location):
    answer = 0
    
    # 큐 생성
    q = deque()
    
    # 우선 순위, 인덱스(location)을 큐에 넣음
    for i in range(len(priorities)):
        q.append((priorities[i],i))
        
    
    while q:
        now, index = q.popleft()
        
        # 큐가 있고, now가 max에서의 우선 순위보다 작다면
        if q and now < max(q,key = lambda x: x[0])[0]:
            # 방금 꺼낸 걸 다시 넣는다.
            q.append((now,index))
    
        else:
            # 방금 꺼낸걸 실행했으므로, 번호표 발급
            answer +=1
            
            # 그 꺼낸 큐가 우리가 원한 그 location이면 answer 반환
            if index == location:
                return answer
    
    
    return answer
            
    
    