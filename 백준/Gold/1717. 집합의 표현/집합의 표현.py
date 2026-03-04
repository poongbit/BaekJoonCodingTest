# 문제 53 집합 표현하기 - 1717번

"""
유니온 파인트리는 부모 리스트를 만들어서 결정한다.
find는 자기 자신을 반환하거나, 재귀함수를 통해 부모님 노드를 찾는다.
union(a,b)는 a의 대장 노드를, b의 대장 노드 소속으로 넣어주는 것이다.

"""


import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6) # 재귀 깊이를 미리 설정해둠

N,M = map(int,input().split())
parent = [i for i in range(N+1)] 

# union 함수 정의

def find(x): # x의 대장 찾아주기
    
    if parent[x] != x: # 대장이 자기 자신이 아닌 경우
        parent[x] = find(parent[x])
        return parent[x]

    else:
        return x # 같으면 자기 자신 반환


def union(parent,a,b): # a의 부모 노드가 b의 부모노드에 들어가게 된다.

    #a,b의 대장을 부름
    root_a = find(a)
    root_b = find(b)

    if root_a != root_b:
        parent[root_a] = root_b # a의 대장은 이제 b의 대장에 속한다.

# 실행

for _ in range(M): # 질의 개수 만큼 반복
    check,a,b = map(int,input().split())

    if check == 0:
        union(parent,a,b)

    elif check == 1:

        if find(a) != find(b):
            print("NO")

        else:
            print("YES")

