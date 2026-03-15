
def solution(numbers, target):
    answer = 0

    def DFS(index,current_sum):
        if index == len(numbers):
            if current_sum == target:
                return 1
            else:
                return 0
        
        return (DFS(index+1,current_sum + numbers[index])
               + DFS(index+1,current_sum - numbers[index]))
    
        
        
                
                
    answer = DFS(0,0)
    
    

    return answer