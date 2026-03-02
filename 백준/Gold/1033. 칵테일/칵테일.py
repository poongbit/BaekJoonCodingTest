# 문제 47 칵테일 만들기 - 1033번

"""
N : 재료의 개수
A : 인접 리스트 # for DFS를 탐색할 지도 구현

visited : DFS를 탐색할 때 탐색 여부 저장 리스트
D (각 노드값 저장 리스트) 

lcm : 최소 공배수


# 최대 공약수 구현

gcd(a,b):
    if b가 0이면
        a가 최대 공약수

    else
        gcd(작은 수, 큰 수 % 작은수) # 재귀 함수 형태로 구현

# 탐색 함수 DFS 구현

    visited 리스트에 현재 노드 방문 기록
    if 현재 노드의 연결 노드 중 방문하지 않은 노드:
        다음 노드값 = 현재 노드의 값 * 비율 로 저장
        DFS(다음 노드)


for 에지 개수 : 
    인접 리스트에 주어진 에지 정보를 저장
    최소 공배수 업데이트


0번 노드에 최소 공배수 저장
0번에서 DFS 탐색 수행

DFS를 이용해 업데이트된 D 리스트의 값들의 최대 공약수 계산
D 리스트의 각 값을 최대 공약수로 나눠 정답 출력

"""


import sys
input = sys.stdin.readline

N = int(input())
A = [[] for _ in range(N)]

visited = [False] * (N)

D = [0] * N

lcm = 1 # 최소 공배수는 1로 지정


# 최대 공약수 함수 구현
def gcd(a,b):
    if b == 0:
        return a

    else:
        return gcd(b,a%b)

"""
노드(Node / 정점): 우리가 들어갈 수 있는 '방'입니다. (예: 1번 방, 2번 방)

엣지(Edge / 간선): 방과 방 사이를 연결하는 '복도'
복도는 투명한 끈처럼 방과 방을 이어주는 논리적인 개념으로만 존재함 (코드상에 직접적으로 존재 x)

복도로 가는게 아니라 방(v)으로 가야 함

"""



# DFS 탐색 함수 구현
def DFS(v):
    
    # 방문 도장 찍기
    visited[v] = True

    for i in A[v]: # A[v] - 현재 방 문을 열고 나갈 수 있는 "연결된 방문들의 목록", 
        # i : (방번호, p,q)
        next = i[0]
        if not visited[next]:
            D[next] = (D[v] * i[2]) // i[1] # 비례식 v : next = p : q 를 풀어서 나온 공식
            DFS(next)



for i in range(N-1):
    a,b,p,q = map(int,input().split())
    A[a].append((b,p,q))
    A[b].append((a,q,p))

    # 데이터를 저장할 때마다 비율과 관련된 수들의 최소 공배수를 업데이트
    lcm *= (p * q // gcd(p,q)) # 최소 공배수는 두 수의 곱을 최대 공약수로 나눈 것


# 모든 p,q의 최소 공배수를 곱하게 해서 소수점으로 안 떨어지게 설정해놓음
D[0] = lcm
DFS(0)
mgcd = D[0]


for i in range(1,N):
    mgcd = gcd(mgcd,D[i])


for i in range(N):
    print(int(D[i] // mgcd), end=' ')


