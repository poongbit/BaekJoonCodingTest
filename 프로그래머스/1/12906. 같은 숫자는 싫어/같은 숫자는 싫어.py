def solution(arr):
    answer = []
    
    stack = []
    
    for item in arr:
        # 만약 아무 것도 없다면 일단 넣음
        if not stack or stack[-1] != item:
            stack.append(item)
        
        if item == stack[-1]:
            pass
            
    
    
    return stack