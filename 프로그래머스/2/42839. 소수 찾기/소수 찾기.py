from itertools import permutations



def solution(numbers):
    answer = 0
    
    num_list = list(numbers)
    num_length = len(num_list) # 숫자의 길이
    
    # 순열로 숫자 생성
    
    found = set() # 중복 숫자는 애초에 못 들어오지 하기 위함
    
    for length in range(1,num_length+1):
        for perm in permutations(num_list,length):
            num = int(''.join(perm)) # 튜플로 되어 있는걸 조인시킴
            found.add(num)
            
    # 에라토스테네스의 체
    # 딱 한번만 생성한다. O(1)로 조회
    max_num = max(found)
    
    is_prime = [True] * (max_num+1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2,int(max_num**0.5)+1):
        if is_prime[i]:
            
            for j in range(i*i,max_num+1,i):
                is_prime[j] = False
                
    
    for i in found:
        if is_prime[i]:
            answer +=1
    
    return answer