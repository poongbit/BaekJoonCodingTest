

def solution(numbers, target):
    answer = 0
    
    # 1. 입출력 받기
    
    count = 0
    
    def DFS(index,current_sum):
        # 모든 숫자를 써야 다 카운트
        if index == len(numbers):
            if current_sum == target:
                # count는 지역변수 복사본이라 밖으로 안나감
                return 1
                
            else:
                return 0
            
        plus = DFS(index+1, current_sum + numbers[index])
        minus = DFS(index+1, current_sum - numbers[index])
        
        return plus + minus
    
    
            
    
    answer = DFS(0,answer)

    return answer