import sys
input = sys.stdin.readline

N = int(input().strip())

M = int(input().strip())

# 모든 도로의 간선 정보를 담는 1차원 배열
graph = []

for _ in range(M):
    a,b,c = map(int,input().split())

    graph.append((c,a,b))


# 최소 비용이 있는 간선부터 차례대로 정렬한다.
graph.sort()


# 그룹을 짓기 위한 부모 노드들 생성

parent = [i for i in range(N+1)]

# 조상님 노드 찾기 
def find(v):
    # 조상님 노드가 자기 자신이 아니면
    if parent[v] != v:
        # 진짜 조상님 노드 찾아 들어간다.
        parent[v] = find(parent[v])

    return parent[v]


def union(a,b):
    root_a = find(a)
    root_b = find(b)

    # 조상님들이 다르면, 같은 조상으로 퉁 친다.
    if root_a != root_b:
        parent[root_a] = root_b

total_cost = 0

for cost, a,b in graph:
    if find(a) != find(b):
        # 같은 그룹으로 퉁치기
        union(a,b)
        total_cost += cost

print(total_cost)
