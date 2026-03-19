from collections import defaultdict

def solution(phone_book):
    answer = True
    
    
    set_phonebook = set(phone_book)
    
    
    for word in set_phonebook:
        for j in range(1,len(word)):
            
            if word[:j] in set_phonebook:
                answer = False
                break
            
    
    
    return answer