import sys

def solution(numbers, target):
    answer = 0
    
    def DFS(i, current_sum):
        # 숫자들을 다 쓴 경우
        if i == len(numbers):
            if current_sum == target:
                return 1
            else:
                return 0
            
        
        return DFS(i+1, current_sum + numbers[i]) + \
        DFS(i+1, current_sum - numbers[i])
            
    answer = DFS(0,0)
        
    

    return answer