from collections import deque

def solution(priorities, location):
    answer = 0
    
    # 큐 생성
    q = deque()
    
    for index in range(len(priorities)):
        q.append((priorities[index],index))

        
    while q:
        prior,index= q.popleft()
        
        if q and prior < max(q,key=lambda x: x[0])[0]:
            # 우선 순위가 더 큰게 있으면 , 꺼낸 건 다시 넣음
            q.append((prior,index))
            
        else:
            # 누군가 실행될 떄마다 번호표가 1 올라감
            answer +=1
            if index == location:
                return answer
            
    
    