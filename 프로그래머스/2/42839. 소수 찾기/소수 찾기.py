from itertools import permutations
import math

def is_prime(n):
    
    if n < 2:
        return False
    
    for i in range(2,int(n**0.5) +1):
        if n % i == 0:
            return False
        
    return True


def solution(numbers):
    answer = 0
    
    # 길이 1짜리, 2짜리, 3자리.. 모든 순열을 만들어야 함
    
    num_list = list(numbers)
    
    found = set()
    
    for length in range(1,len(num_list)+1):
        for perm in permutations(num_list,length):
            num = int(''.join(perm))
            if is_prime(num) and num not in found:
                answer +=1
                found.add(num)
                
    
    return answer