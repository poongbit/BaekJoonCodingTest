import sys
input = sys.stdin.readline


N,W,H,L = map(int,input().split())

# 단순한 넓이 나누기로 안된다.

# 가로로 몇 마리, 세로에 몇 마리 들어가는 지도 따로 계산

cols = W//L
rows = H//L


# 최대 수용 가능한 소의 수
max_cows = cols * rows

# N마리가 다 들어갈 수 있으면 1, 아니면 0

print(min(N,max_cows)) # 공간이 더 많아도 소보다 더 많으면 입주가 안됨