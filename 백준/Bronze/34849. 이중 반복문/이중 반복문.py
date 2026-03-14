import sys
input = sys.stdin.readline


calculate = 1e8


n = int(input())

com_cal = n**2

if com_cal <= calculate:
    print("Accepted")

else:
    print('Time limit exceeded')