from collections import deque

def solution(begin, target, words):
    answer = 0
    
    # 무엇을 결정해야 하는 가?
    # 알파벳 하나만 바꿔서 words에 있는 걸로 바꿀 수 있는 지 
    
    # 종료 조건은 무엇인가?
    # 바꾼 단어가 target과 똑같은지
    
    # 끝났을 떄 뭘 체크해야 하는가?
    
    # 단어들을 다 체크했는 지 확인
    visited = [False] * len(words)
    
    # 알파벳 차이가 1일 때 단어를 변경함
    def is_convertible(a,b):
        diff = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                diff +=1
                
        return True if diff == 1 else False
    
    
    # words의 방문 도장
    visited = [False] * (len(words))
    
    def BFS():
        # 큐 스택 초기화
        q = deque()
        
        
        count = 0 
        
        q.append((begin,count))
        
        while q:
            start, count = q.popleft()
            
            if start == target:
                return count
            
            
            for i in range(len(words)):
                if not visited[i] and is_convertible(start, words[i]):
                    visited[i] = True
                    q.append((words[i],count+1))
        
        
        return 0
        
        
    answer = BFS()
        
        
    
    return answer

    
    