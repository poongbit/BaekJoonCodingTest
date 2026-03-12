from itertools import permutations

def solution(k, dungeons):
    answer = -1
    
    
    for perm in permutations(dungeons):
        piro = k
        count = 0
        for min_piro, dun_piro in perm:
            if min_piro <=piro:
                piro -= dun_piro
                count +=1
        
        answer = max(answer,count)
    
    return answer