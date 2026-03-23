from collections import deque
def solution(begin, target, words):
    
    """
    3개중 두 개 맞으면 True로 반환하는 함수 만들기
    
    # 멈춤 조건:
        바꾼게 타겟과 같으면 멈춤
        맞으면 반환
    
    """
    
    visited = [False] * len(words)
    
    
    def is_convertible(a,b):
        num = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                num +=1
        
        if num ==1:
            return True
        else:
            return False
        
    def DFS():
        q = deque()
        q.append(begin)
        count = 0

        while q:
            now_word = q.popleft()

            if now_word == target:
                return count

            for i in range(len(words)):
                if is_convertible(now_word,words[i]) and not visited[i]:
                    visited[i] = True
                    count +=1
                    q.append(words[i])
        
        return 0
    
    
    answer = DFS()
        
    return answer
        

    
    