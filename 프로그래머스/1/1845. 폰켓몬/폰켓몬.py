import itertools

def solution(nums):
    answer = 0
    
    # 포켓몬 종류 set으로 표현
    
    set_poko = set(nums)
    
    # 골라야 하는 포켓몬 개수:
    choose = len(nums) // 2
    
    if len(set_poko) >= choose:
        answer = choose
        
    else:
        answer = len(set_poko)
    
    
    
    
    return answer