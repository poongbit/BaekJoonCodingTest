words = []
vowels = ['A','E','I','O','U']

def dfs(word):
    
    # 길이가 5인 글자도 붙혀야 함
    
    words.append(word)
    
    if len(word) == 5:
        return
    
    for v in vowels:
        dfs(word + v) # 깊이 들어가면서 for 구문이 A,A,A로 걸린다.
        

def solution(word):
    answer = 0
    
    for v in vowels:
        dfs(v)
    
    
    for index, dic_word in enumerate(words):
        if word == dic_word:
            answer = index +1
            break
    
    
    return answer