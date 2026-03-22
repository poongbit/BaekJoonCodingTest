def solution(triangle):
    answer = 0
    
    # dp[n][k] : n번째 줄에서 k번쨰를 골랐을 떄의 수
    
    
    """
      0 -based로 다시 세기
      
      dp[0][0] = triagle[0][0] = 7
      
      
      dp[1][0] = dp[0][0] + triangle[1][0]
      dp[1][1] = dp[0][0] + triangle[1][1]
      
      왼쪽 빗변:
      dp[2][0] = dp[1][0] + triangle[2][0]
      
      사이의 값들:
      dp[2][1] = dp[1][0] + triangle[2][1]
                    or dp[1][1] + triangle[2][1]
    
      오른쪽 빗변:
      dp[2][2] = dp[1][1] + triangle[2][2]
      
      
      왼쪽 빗변
      dp[3][0] = dp[2][0] + triangle[3][0]
      
      그 사이 값
      dp[3][1] = dp[2][0] + triangle[3][1]
                or dp[2][1] + triangle[3][1]
                
     d[3][2] = dp[2][1] + triangle[3][2]
                or dp[2][2] + triangle[3][2]
                
    오른쪽 빗변
    dp[3][3] = dp[2][2] + triangle[3][3]
      
      
     
    왼쪽 빗변 :
    dp[n][0] = dp[n-1][0] + triangle[n][0]
    
    오른쪽 빗변 :
    dp[n][n] = dp[n-1][n-1] + triangle[n][n]
    
    사이 값들 점화식:
    k는 (1 ~ n-1까지)
    
    ex) k = 1
    
    dp[n][k] = dp[n-1][k-1] + triangle[n][k]
                or dp[n-1][k] + triangle[n][k]
    
    
    """
    
    # 이중 배열이 필요함
    dp = [[0] * len(row) for row in triangle]
    
    
    # 가장 맨 꼭대기, 왼쪽, 오린쪽 초기 빗변
    dp[0][0] = triangle[0][0]
    dp[1][0] = dp[0][0] + triangle[1][0]
    dp[1][1] = dp[0][0] + triangle[1][1]
    
    heights = len(triangle)
    
    if heights == 1:
        return dp[0][0]
    
    if heights == 2:
        return max(dp[1][0], dp[1][1])
    
    # 3층 이상인 경우
    
    for n in range(2,heights):
        # 각 빗변 구하기 - 왼쪽, 오른쪽
        dp[n][0] = dp[n-1][0] + triangle[n][0]
        dp[n][n] = dp[n-1][n-1] + triangle[n][n]
        
        # 빗변 사이에 있는 값 구하기
        for k in range(1,n):
            left = dp[n-1][k-1] + triangle[n][k]
            right = dp[n-1][k] + triangle[n][k]
            
            dp[n][k] = max(left,right)
        
    result = []
    
    for item in dp[n]:
        result.append(item)
        
    result.sort()
    
    answer = result[-1]
        
    
    return answer