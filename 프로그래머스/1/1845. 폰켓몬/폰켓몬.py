import itertools
from itertools import permutations, combinations

def solution(nums):
    answer = 0
    
    set_nums = set(nums)
    
    pick = len(nums) // 2
    
    # 전체 종류 수 = len(set_nums)
    
    if len(set_nums) > pick:
        answer = pick
    
    else:
        answer = len(set_nums)
    
    
    
    return answer