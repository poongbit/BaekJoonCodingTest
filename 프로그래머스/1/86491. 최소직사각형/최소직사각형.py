def solution(sizes):
    answer = 0
    
    max_w = 0
    max_h = 0
    
    max = 0
    
    for weight,height in sizes:
        
        if weight < height:
            weight, height = height,weight
    

        if max_w <= weight:
            max_w = weight
            
        else:
            pass
        
        if max_h <= height:
            max_h = height
            
        else:
            pass
        
        
        
    answer = max_w * max_h
    

    return answer
