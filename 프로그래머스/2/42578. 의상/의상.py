from itertools import combinations
from collections import defaultdict

def solution(clothes):
    answer = 0
    
    wear_style = defaultdict(int)
    kind_style = set()
    
    
    # 값 부여하기
    for item, style in clothes:
        wear_style[style] += 1
        
    # 곱셈 누적
    result = 1
    for count in wear_style.values():
        result *= (count + 1) # 안 입음 포함
        
    answer = result -1
        
    
    
    
    
    """
    최소 한 가지 옷을 입는다.
    
    ex) headgear 종류 2가지, eyewear 1가지
    headgear a, b, 아무것도 안 입기 - 3
    eyewear c, 아무것도 안 입기 - 2
    
    3 x 2 = 6, 여기서 둘 다 안 입기는 빼야 하므로 -1 해야 함
    
    
    """

    
    
    
    
    
    
    return answer