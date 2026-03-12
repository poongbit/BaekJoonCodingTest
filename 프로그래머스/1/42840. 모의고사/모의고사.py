def solution(answers):
    answer = []
    
    # 문제의 수
    num_quiz = len(answers)
        
    # 1,2,3번 학생 찍기
    student_1 = [1,2,3,4,5] * num_quiz
    student_2 = [2,1,2,3,2,4,2,5] * num_quiz
    student_3 = [3,3,1,1,2,2,4,4,5,5] * num_quiz
    
    # 1,2,3번 학생의 정답 맞춘 개수
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
            

    max_count = max(count_1,count_2,count_3)
        
    for i, count in enumerate([count_1,count_2,count_3]):
        if max_count == count:
            answer.append(i+1)
    
    
    return answer