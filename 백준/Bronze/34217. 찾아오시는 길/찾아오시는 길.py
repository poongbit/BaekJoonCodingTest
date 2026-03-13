import sys
input = sys.stdin.readline

"""

출발지 - 한양대역 A
출발지 - 용달역 B

한양대 - ITBT C
용답역 - ITBT D



"""

A,B = map(int,input().split())
C,D = map(int,input().split())

hangyang = A+C
yong = B + D


if hangyang == yong:
    print('Either')

elif hangyang > yong:
    print('Yongdap')

else:
    print('Hanyang Univ.')