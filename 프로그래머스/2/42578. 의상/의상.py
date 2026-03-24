from collections import defaultdict

def solution(clothes):
    answer = 0
    
    # 사전으로 종류와 개수를 기록하고
    # 경우의 수로 곱한다. 0,1,2개 선택하는 경우까지
    
    fashion = defaultdict(int)
    
    for cloth, style in clothes:
        fashion[style] +=1
        
    # 곱하기를 위한 변수 선언
    result = 1
    for style, count in fashion.items():
        result *= count + 1 #(아무 것도 선택 안하는 것 포함)
    
    answer = result - 1 #(전부 다 안 고른 경우 뺴줌)
    
    return answer