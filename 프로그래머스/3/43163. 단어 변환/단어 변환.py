from collections import deque

def solution(begin, target, words):
    answer = 0
    
    
    if target not in words:
        return 0
    
    # 단어 수 만큼 방문 도장 찍기
    visited = [False] * len(words)
    
    
    # 두 단어가 한 글자만 다른지 체크하는 함수
    def is_convertible(a,b):
        diff = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                diff +=1
    
        return diff == 1
    
    q = deque()
    q.append((begin,0))
    
    while q:
        word, count = q.popleft()
        
        if word == target:
            return count
        
        
        for i in range(len(words)):
            if not visited[i] and is_convertible(word,words[i]):
                visited[i] = True
                q.append((words[i],count+1))
    
    
    return 0
    

    
    