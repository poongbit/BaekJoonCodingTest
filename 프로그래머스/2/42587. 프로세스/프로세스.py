from collections import deque

def solution(priorities, location):
    answer = 0
    
    # 큐 생성
    q = deque()
    
    for i in range(len(priorities)):
        # 우선순위, 인덱스 추가 
        q.append((priorities[i],i))
    
    # [2, 1, 3, 2], location = 2
    
    count = 0
    
    #print(q[0])
    # 	(2, 0)
    
    while q:
        base, index = q.popleft()
        
        # 전 순회를 해서 base가 가장 높은 우선순위 인지를 체크
        
        if q and base < max(q,key=lambda x: x[0])[0]:
            # 다시 집어넣기
            q.append((base,index))
            
        else:
            count +=1
            if index == location:
                answer = count
                break
    
    
    return answer
            
    
    