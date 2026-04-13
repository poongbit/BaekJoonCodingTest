import sys
input = sys.stdin.readline

stage1 = str(input().strip())
stage2 = str(input().strip())

if stage1 == stage2:
    print(0)

else:
    print(1550)