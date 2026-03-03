import sys

input = sys.stdin.readline

A,T = map(int,input().split())


P = 10 + 2 * (25 - A + T)

if P < 0:
    print(0)

else:
    print(P)