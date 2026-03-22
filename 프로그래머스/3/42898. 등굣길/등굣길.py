def solution(m, n, puddles):
    answer = 0
    
    """
    
    dp[y][x] : (1,1)에서 (x,y)까지 도달할 수 있는 경로의 가짓수
    
    dp[1][1] : 여기에 있는 경우의 수는 한 가지 방법으로 존재함
    
    여기에 도착하기 위해 윗방에서 정보를 꺼내와야 함
    dp[y][x] = dp[y-1][x] + dp[y][x-1]
    
    if x, y == puddles[0],puddles[1]:
        dp[y][x] = 0
    
    
    """
    
    dp = [[0] * (m+1) for _ in range(n+1)]
    
    # (1,1) 좌표에 도달하는 경우의 수는 1가지 
    dp[1][1] = 1
    
    for y in range(1,n+1):
        for x in range(1,m+1):
            
            if y == 1 and x == 1:
                continue
            
            if [x,y] in puddles:
                dp[y][x] = 0
                continue
                
            dp[y][x] = (dp[y-1][x] + dp[y][x-1]) % 1000000007
            
            
    answer = dp[n][m]
    
    
    return answer