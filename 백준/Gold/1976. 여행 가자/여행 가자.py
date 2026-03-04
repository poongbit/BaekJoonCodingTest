import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
M = int(input())

parent = [i for i in range(N+1)]

# find 함수 작성하기

def find(x): # 대장 노드 찾기 
    
    # 부모 노드가 자기 자신이 아니면, 재귀를 통해 더 파고들어간다.
    if parent[x] != x:
        parent[x] = find(parent[x])
        return parent[x]

    # 아니면 자기 자신을 반환

    return x


def union(a,b):
    # a,b의 대장들을 각각 부름
    root_a = find(a)
    root_b = find(b)

    if root_a != root_b:
        parent[root_a] = root_b




# 도시 연결 정보(행렬) 처리
for i in range(1,N+1):
    row = list(map(int,input().split())) # i번째 도시와 다른 도시들의 연결 정보

    for j in range(len(row)): # row 안에 있는 인덱스 불러오기
        if row[j] == 1: # i번 도시와 j+1번 (index + 1번)
            union(i,j+1) # 두 도시를 하나의 집합으로 합친다.


# 여행 계획 확인
plan = list(map(int,input().split())) # 여행 경로 ex) (1,2,3)

# 여행 계획의 첫 번째 도시의 대장을 찾는다.
root = find(plan[0])

possible = True

for i in range(1,M):
    if find(plan[i]) != root: # 다른 가문의 도시가 하나라도 껴 있다면?
        possible = False
        break

# 결과 출력
if possible: print("YES")
else: print("NO")
