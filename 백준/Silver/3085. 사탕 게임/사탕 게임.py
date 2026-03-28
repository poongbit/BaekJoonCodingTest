import sys
input = sys.stdin.readline

n = int(input().strip())

graph = [[0] * (n) for _ in range(n)]

for i in range(n):
    line = input().strip()

    for j in range(len(line)):
        graph[i][j] = line[j]



# 복잡한 것이 있다면 함수로 지정하라



def change(graph):

    count = 0

    # 행 기준으로 바꾸기
    for i in range(n):
        cur = 1
        
        for j in range(1,n):
            if graph[i][j] == graph[i][j-1]:
                cur +=1

            else:
                # 이어진게 끊어짐
                cur = 1


            count = max(cur,count)

    # 열 기준으로 바꾸기
    for i in range(n):
        cur = 1

        for j in range(1,n):
            if graph[j][i] == graph[j-1][i]:
                cur +=1

            else:
                # 이어진게 끊어짐
                cur = 1

            count = max(cur,count)


    return count

ans = 0

for i in range(n):
    for j in range(n):

        # 행 기준으로 한번 체크
        # 인덱스를 안 벗어나고, 그 두개가 다를 경우
        if j+1<n and graph[i][j] != graph[i][j+1]:
            # 스왑해보기
            graph[i][j], graph[i][j+1] = graph[i][j+1], graph[i][j]
            ans = max(ans, change(graph))
            # 다시 원래대로 복구하기
            graph[i][j], graph[i][j+1] = graph[i][j+1], graph[i][j]

        # 열 기준으로 바꾸기
        if i+1 < n and graph[i][j] != graph[i+1][j]:
            # 스왑해보기
            graph[i][j], graph[i+1][j] = graph[i+1][j], graph[i][j]
            ans = max(ans,change(graph))
            # 다시 원상태로 복구하기
            graph[i][j], graph[i+1][j] = graph[i+1][j], graph[i][j]


print(ans)