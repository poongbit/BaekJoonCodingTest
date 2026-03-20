def solution(s):
    answer = True
    stack = []
    count = 0
    
    for letter in s:
        if letter == '(':
            stack.append(letter)
            count +=1
            
        else:
            if stack == []:
                answer = False
                break
            
            else:
                stack.pop()
                count -=1
                
    
    if answer == False:
        answer = False
    
    else:
        if count == 0:
            answer = True
        
        else:
            answer = False
            
    return answer
