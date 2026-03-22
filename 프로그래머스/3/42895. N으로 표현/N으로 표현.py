def solution(N, number):
    # N이랑 number가 같은 경우
    if N == number:
        return 1
    
    # dp[k] : 숫자 N을 k번 사용했을 때, 나오는 결과값
    # number가 나오는 가장 최초의 dp[k]를 구하고, k를 반환한다.
    
    # N을 1번, 2번, ..., 9번 쓰는 경우를 나눠서 체크
    dp = [set() for _ in range(9)]
    
    for i in range(1,9):
        # N, NN, NNN 같은 형태 만들기
        dp[i].add(int(str(N) * i))
        
        for j in range(1,i):
            # 1번 뭉치와 2번 뭉치를 꺼내기
            for x in dp[j]:
                for y in dp[i-j]:
                    dp[i].add(x + y)
                    dp[i].add(x - y)
                    dp[i].add(x * y)
                    
                    if y !=0:
                        dp[i].add(x//y)
                        
            if number in dp[i]:
                return i
            
    return -1
                    
                    
                    
                
    
    
    
    
    