import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6) 
"""

0,1,2,....,n
"""

n,m = map(int,input().split())

# 부모 노드 생성
parent = [i for i in range(n+1)]

def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])

    return parent[v]

def union(a,b):
    root_a = find(a)
    root_b = find(b)

    if root_a != root_b:
        parent[root_a] = root_b




for _ in range(m):    
    check,a,b = map(int,input().split())
    # 0이면 합치기
    if check == 0:
        union(a,b)

    elif check == 1:
        if find(a) != find(b):
            print('NO')

        else:
            print('YES')


