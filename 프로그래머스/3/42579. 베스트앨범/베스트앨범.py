from collections import defaultdict

def solution(genres, plays):
    answer = []
    
    """
    클래식, 팝 둘 중 어느게 가장 많이 들었는 지 확인
    딕셔너리 활용?
    
    그 후, 각 카테고리 별로 plays 고유 번호 순으로 정렬하기 
    딕셔너리 내에서 정렬시키기?
    
    """
    
    music_played = defaultdict(int)
    
    for i in range(len(plays)):
        music_played[genres[i]] += plays[i]
    
    # 가장 많은 카테고리 순으로 정렬하기
    result = []
        
    for key, value in music_played.items():
        result.append((key,value))
    
    result.sort(key=lambda x : x[1], reverse = True)
    
    
    music_genre = []
    
    for key, value in result:
        music_genre.append(key)
    
     # genres, plays와 1 대 1 매칭시키기?
    
    music_list = defaultdict(list)
    
    
    for i in range(len(genres)):
        # 재생 수, 고유 번호 연결
        music_list[genres[i]].append((plays[i],i))
        
    
    for genre in music_genre:
        count = 1
        music_list[genre].sort(key = lambda x : x[0],reverse = True)
        
        for plays, index in music_list[genre]:
            if count > 2:
                break
            answer.append(index)
            count +=1
    
    
    
    

    return answer