def solution(s):
    stack = []
    
    for letter in s:
        if letter == '(':
            stack.append(letter)
            
        else:
            if not stack:
                return False

            else:
                stack.pop()
    
    return not stack
                
