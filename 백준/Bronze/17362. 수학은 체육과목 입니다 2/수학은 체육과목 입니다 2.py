import sys
input = sys.stdin.readline


n = int(input())

index = (n-1) % 8

answer = ['1','2','3','4','5','4','3','2']


print(answer[index])