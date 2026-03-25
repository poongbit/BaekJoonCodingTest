def solution(prices):
    answer = [0] * len(prices)
    
    # 인덱스 저장하는 변수
    stack = []
    
    for i, price in enumerate(prices):
        # 현재 가격이 마지막에 저장했던 price[index] 보다 작으면, 떨어진 것
        while stack and prices[stack[-1]] > price:
            j = stack.pop()
            answer[j] = i - j
            
        stack.append(i)
    
    # 어디 걸리는 거 없이 끝까지 증가한 price들의 인덱스
    while stack:
        j = stack.pop()
        
        answer[j] = len(prices)-1 - j
    
    return answer
            
