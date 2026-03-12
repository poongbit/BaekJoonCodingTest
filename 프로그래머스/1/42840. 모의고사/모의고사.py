def solution(answers):
    answer = []
        
    # 1번 수포자 찍기
    
    num_quiz = len(answers)
    
    student_1 = [1,2,3,4,5] * num_quiz
    student_2 = [2,1,2,3,2,4,2,5] * num_quiz
    student_3 = [3,3,1,1,2,2,4,4,5,5] * num_quiz
    
    
    count_1 = 0
    count_2 = 0
    count_3 = 0
    
    for i in range(num_quiz):
        if student_1[i] == answers[i]:
            count_1 +=1
            
    
    for i in range(num_quiz):
        if student_2[i] == answers[i]:
            count_2 +=1
            
    for i in range(num_quiz):
        if student_3[i] == answers[i]:
            count_3 +=1
        
    
    # 최댓값 구하고, 그 최댓값과 같은 학생만 추가
    max_count = max(count_1, count_2,count_3)
    
    for i, count in enumerate([count_1,count_2,count_3]):
        if count == max_count:
            answer.append(i+1)

    
    
    return answer