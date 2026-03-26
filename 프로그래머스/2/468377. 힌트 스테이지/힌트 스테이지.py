# 비트마스킹 연습하기

def solution(cost, hint):
    n = len(cost)
    result = float('inf')
    
    # 1 << k -> 2^k승 (고를지 말지 경우의 수)
    for mask in range(1 << n-1):
        # 어느 힌트 번들을 구매할 지에 대한 걸 결정한 상태에서 합 계산
        # 일단 스테이지 1에서는 힌트권이 없으므로 비용은 그대로 계산
        # 힌트의 개수를 담는 공간
        hints = [0] * (n+1)
        total = 0
        # 1 ~ n-1 스테이지 까지
        for i in range(0,n):
            # i 스테이지에서, 힌트 구매를 얼마나 할 건지
            hint_use = min(hints[i+1],n-1)
            total += cost[i][hint_use]
            
            if i < n-1 and (mask >> i) & 1:
                # 번들 가격 더하기 
                total += hint[i][0]
                
                # 번들 안에 있는 힌트들
                for h in hint[i][1:]:
                    hints[h] +=1
                
        result = min(result,total)    
        
    return result