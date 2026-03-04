import sys


input = sys.stdin.readline


N,A,B = map(int,input().split())


bus_wait = A
arrive_subway = 0


if N == B: # 지하철을 타러 걸어가다가 놓치면
    arrive_subway = N

elif N < B:
    arrive_subway = B




if bus_wait > arrive_subway:
    print("Subway")

elif bus_wait == arrive_subway:
    print('Anything')


else:
    print("Bus")

