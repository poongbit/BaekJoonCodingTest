def solution(phone_book):
    answer = True
    
    # 반복적으로 번호를 탐색해야 하므로
    set_phonebook = set(phone_book)
    
    for word in set_phonebook:
        
        word_length = len(word)
        
        for i in range(1,len(word)):
            if word[:i] in set_phonebook:
                answer = False
                break
    
    return answer