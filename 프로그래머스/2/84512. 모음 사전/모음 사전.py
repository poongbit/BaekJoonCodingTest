words = [] # 전역으로 뺴기
vowels = ['A','E','I','O','U']


def dfs(current):
    
    words.append(current) # 현재 단어를 목록에 추가
    
    if len(current) == 5:
        return 
    
    for v in vowels:
        dfs(current + v) # 다음 글자 붙히기
        
    

def solution(word):
    answer = 0
    
    
    for v in vowels:
        dfs(v)
        
    for i, dic_word in enumerate(words):
        if word == dic_word:
            answer = i + 1
            break
    
    
    return answer