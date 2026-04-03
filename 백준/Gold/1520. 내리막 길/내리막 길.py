import sys
input = sys.stdin.readline
sys.setrecursionlimit(500 * 500 + 100)
# 경로의 개수? 이거 dp 활용?

"""
 dp[row][column] : row와 column에 도달 할 수 있는
 경우의 수


"""

# 세로 : M, 가로 : N
M,N = map(int,input().split())

graph = []

for _ in range(M):
    line = list(map(int,input().split()))

    graph.append(line)




# 방문 안한 경우를 -1로 체크해서 표시
dp = [[-1] * (N+1) for _ in range(M+1)]


def DFS(row,column):
    if row == M-1 and column == N-1:
        dp[row][column] = 1
        return dp[row][column]
    
    elif dp[row][column] != -1:
        return dp[row][column]
    
    dp[row][column] = 0

    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    for i in range(4):
        new_row = row + dy[i]
        new_column = column + dx[i]

        if 0<=new_row<M and 0<=new_column<N:

            if graph[new_row][new_column] < graph[row][column]:
                 dp[row][column] += DFS(new_row,new_column)


    return dp[row][column]


print(DFS(0,0))


