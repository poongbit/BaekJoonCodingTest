from collections import defaultdict


def solution(genres, plays):
    answer = []
    
    # 장르별 총 재생 수
    total = defaultdict(int)
    
    for i in range(len(plays)):
        total[genres[i]] += plays[i]
    
    
    total = sorted(total.items(),key= lambda x : x[1],reverse = True)
    
    
    # 장르별 곡 목록 (고유번호, 재생 수)
    music_number = defaultdict(list)
    
    for i in range(len(plays)):
        music_number[genres[i]].append((i,plays[i]))
        
    
    
    # 장르 총 재생 수 내림차순 정렬, 장르별로 따로 정렬해야 함
    
    for genre in music_number.keys():
        music_number[genre] = sorted(music_number[genre],key = lambda x : x[1],reverse= True)
        
    
    
    for genre, _ in total:
        for idx, _ in music_number[genre][:2]:
            # pop 일 때 : [(4,2500),(1,600)]
            # classic 일 때 : [(3,800),(0,500)]
            
            answer.append(idx)
            
    
    

    return answer