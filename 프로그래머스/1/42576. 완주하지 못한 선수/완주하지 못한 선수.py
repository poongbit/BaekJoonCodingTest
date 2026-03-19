def solution(participant, completion):
    answer = ''
    
    participant.sort()
    completion.sort()
    
    flag = True
    
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
            flag = False
            break
    
    if flag:
        answer = participant[-1]
        
    
    return answer