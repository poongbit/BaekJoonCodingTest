def solution(phone_book):
    answer = True
    
    # phonebook의 번호를 set()으로 저장해서 탐색 시간 줄이기
    set_phonebook = set(phone_book)
    
    for item in set_phonebook:
        # 각 단어의 길이 체크
        length = len(item)
        
        for i in range(1,length):
            
            if item[:i] in set_phonebook:
                return False
                
    
    
    return answer