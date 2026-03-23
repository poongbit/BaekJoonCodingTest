from collections import defaultdict
def solution(participant, completion):
    answer = ''
    
    participant_attend = defaultdict(int)
    
    for member in participant:
        participant_attend[member] +=1
        
    for member in completion:
        participant_attend[member] -=1
        
    for i in range(len(participant)):
        if participant_attend[participant[i]] !=0:
            answer = participant[i]
    
    return answer