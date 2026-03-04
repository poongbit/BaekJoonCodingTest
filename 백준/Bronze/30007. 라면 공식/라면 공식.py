import sys
input = sys.stdin.readline


N = int(input())


for _ in range(N):
    A,B,X = map(int,input().split())

    answer = A*(X-1) + B
    print(answer)