# 문제 55 - 거짓말쟁이가 되긴 싫어 1043번

"""
관계의 연쇄작용

1. 그룹화 :"A와 B가 같은 파티에 있다', "A와 B가 친구다"처럼 요소를 묶어야 할 때
2. 연쇄 반응 : "A와 B가 연결되고, B와 C가 연결되면 A와 C도 같은 팀이다" 라는 논리가 필요할 때
3. 대표자 확인 : 이 그룹에 진실을 아는 사람' 이라는 대장이 포함되어 있는가를 확인해야 할 때


모든 인맥 지도를 유니온 파인드로 다 그려넣고, 지도를 완성한 후에, 진실을 아는 사람들의 대장을 찾아서
그 대장과 연결된 모든 노드를 "오염된 구역"으로 선포한다.

"""

# 1. 초기화
import sys
input = sys.stdin.readline


N,M = map(int,input().split())

truth_info = list(map(int,input().split()))
truth_knowers = truth_info[1:]


def find(x):

    if parent[x] != x:
        parent[x] = find(parent[x])

        return parent[x]

    else:
        return x

def union(a,b):

    root_a = find(a)
    root_b = find(b)

    if root_a != root_b:
        parent[root_a] = root_b
    

# 대장 노드 초기화
parent = [i for i in range(N+1)]

parties = [] # 각 파티에 참석한 사람들의 정보를 담을 리스트

# 2. 파티의 정보를 읽으며 "같은 파티 사람들"을 하나로 합치기

for _ in range(M):
    party_info = list(map(int,input().split()))

    attendees = party_info[1:]
    parties.append(attendees) # 나중에 다시 확인해야 하므로 저장

    # 파티에 온 사람들 전부 한 가문으로 묶음

    for i in range(len(attendees) - 1):
        union(attendees[i],attendees[i+1])


# 3. 진실을 아는 사람들의 "진짜 대장(Root)"을 찾아서 표시하기
# 누가 진짜 위험한 대장들인지 리스트업

danger_roots = []
for person in truth_knowers:
    danger_roots.append(find(person))

# 4. 모든 파티를 돌며 "거짓말 할 수 있는 파티" 카운트
count = 0 
for attendees in parties:
    can_lie = True # 플래그

    for person in attendees:
        # 이 사람의 대장이 '진실을 아는 가문'의 대장과 같다면?
        if find(person) in danger_roots:
            can_lie = False
            break

    if can_lie:
        count +=1

print(count)