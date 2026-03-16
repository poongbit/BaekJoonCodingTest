import sys
input = sys.stdin.readline

T,X = map(int,input().split())

N = int(input())

for _ in range(N):
    K = int(input())

    flag = True
    
    row = list(map(int,input().split()))

    if X not in row:
        flag = False
        break

    


if flag:
    print("YES")

else:
    print('NO')

    
        
    
