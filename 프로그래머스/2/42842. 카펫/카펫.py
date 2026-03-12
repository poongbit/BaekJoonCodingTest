def solution(brown, yellow):
    answer = []
    
    
    """
    갈색 : 가로 x 2 + 세로 x 2 - 4
    노랑 : 전체 칸 - 갈색
    
    가로 x 세로 = brown + yellow
    
    for 가로 in range(?,total+1):
        세로 = total // 가로
    
    """
    
    total = brown + yellow
    
    for garo in range(3,total+1):
        sero = total // garo
        
        if garo * sero == total and (brown == garo * 2 + sero * 2 -4) and garo>=sero:
            answer.append(garo)
            answer.append(sero)
            break
    
    
    
    return answer