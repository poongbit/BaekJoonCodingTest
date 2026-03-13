count = 0

def DFS(index,current_sum,numbers,target):
    
    if index == len(numbers):
        if current_sum == target:
            global count
            count +=1

        return

    DFS(index+1,current_sum + numbers[index],numbers,target)
    DFS(index+1,current_sum - numbers[index],numbers,target)
    


def solution(numbers, target):
    answer = 0
    
    DFS(0,0,numbers,target)
    
    answer = count
    

    return answer