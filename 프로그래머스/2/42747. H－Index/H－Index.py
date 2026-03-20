def solution(citations):
    answer = 0
    
    citations.sort(reverse= True)
    
    for i in range(len(citations)):
        cited = i+1
        
        if citations[i] >= cited:
            answer = cited
            
        else:
            break
    
    
    
    return answer