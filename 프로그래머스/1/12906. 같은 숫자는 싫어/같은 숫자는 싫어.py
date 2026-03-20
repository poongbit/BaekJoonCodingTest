def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    
    for i in range(len(arr)):
        if answer == [] or answer[-1] != arr[i]:
            answer.append(arr[i])
        
        elif answer[-1] == arr[i]:
            continue
            
    
    
    return answer