from collections import defaultdict


def solution(genres, plays):
    answer = []
    
    # 가장 많이 팔린 순서대로 장르 순 구하기
    music_genre = defaultdict(int)
    
    for i in range(len(plays)):
        music_genre[genres[i]] += plays[i]
    
    # 가장 많이 팔린 순으로 정렬
    music_genre = sorted(music_genre.items(), key = lambda x : x[1], reverse = True)
    
    
    # 한 음악 장르에서 가장 많이 들은 음악 순으로 정렬
    genre_played = defaultdict(list)
    
    for i in range(len(plays)):
        genre_played[genres[i]].append((i,plays[i]))
        
    
    # 각 key값마다 value에서 정렬하기
    
    for key in genre_played.keys():
        genre_played[key] = sorted(genre_played[key], key = lambda x : x[1],reverse = True)
        
    
    for key, _ in music_genre:
        for index, played in genre_played[key][:2]:
            answer.append(index)
            
    

    return answer