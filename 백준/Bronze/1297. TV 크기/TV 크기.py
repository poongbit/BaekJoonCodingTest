import sys
input = sys.stdin.readline

"""
D : 대각선의 길이
H : 높이 비율
W : 너비 비율


D^2 = (H*k)^2 + (W*k)^2

D^2 = k^2(H^2 + W ^2)


D^2 / (H^2 + W^2) = k^2

루트

D / root(H^2 + W^2) = k


"""



# 1. 데이터 입력받기
D, H, W = map(int,input().split())


# 2. 수학식 계산하기


k = D / ((H**2 + W**2) ** 0.5)


print(int(k * H), end= " ")
print(int(W*k))
