import sys
input = sys.stdin.readline

n = int(input().strip())

candy_graph = [[0] * (n) for _ in range(n)]

for i in range(n):
    line = input().strip()

    for j in range(len(line)):
        candy_graph[i][j] = line[j]



def max_count(graph):
    # 모든 행, 모든 열을 순회하면서
    # 연속으로 같은 색이 몇 개인지 세기
    # 최댓값 변환

    count = 0

    # 행 방향 비교하기
    for i in range(len(graph)):
        cur = 1
        for j in range(1,len(graph)):
            # 옆에꺼 비교하기
            if graph[i][j] == graph[i][j-1]:
                cur +=1

            else:
                cur = 1 # 연속 끊기면 리셋

            count = max(count,cur)


    for i in range(len(graph)):
        cur = 1
        for j in range(1,len(graph)):
            if graph[j][i] == graph[j-1][i]:
                cur +=1

            else:
                cur = 1 # 연속 끊기면 리셋

            count = max(count,cur)


    return count

ans = 0

for i in range(n):
    for j in range(n):

        if j + 1 < n and candy_graph[i][j] != candy_graph[i][j+1]:
            candy_graph[i][j], candy_graph[i][j+1] = candy_graph[i][j+1], candy_graph[i][j]
            ans = max(ans,max_count(candy_graph))
            candy_graph[i][j], candy_graph[i][j+1] = candy_graph[i][j+1], candy_graph[i][j]

        if i+1 < n and candy_graph[i][j] != candy_graph[i+1][j]:
            candy_graph[i][j], candy_graph[i+1][j] = candy_graph[i+1][j], candy_graph[i][j]
            ans = max(ans,max_count(candy_graph))
            candy_graph[i][j], candy_graph[i+1][j] = candy_graph[i+1][j], candy_graph[i][j]


print(ans)
