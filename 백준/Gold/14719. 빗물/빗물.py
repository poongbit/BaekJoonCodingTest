import sys
input = sys.stdin.readline

y,x = map(int,input().split())

# 그래프 그리기

height = list(map(int,input().split()))

# 왼쪽 배열, 오른쪽 배열 채우기

left_max = [0] * x
right_max = [0] * x


# 왼쪽 배열부터, 최대 배열 추가하기
left_max[0] = height[0]

for i in range(1,x):
    left_max[i] = max(left_max[i-1],height[i])


# 오른쪽 배열부터 최대 배열 추가하기
right_max[x-1] = height[x-1]

for j in range(x-2,-1,-1):
    right_max[j] = max(right_max[j+1],height[j])

ans = 0

for i in range(x):
    answer = min(left_max[i],right_max[i]) - height[i]

    if answer > 0:
        ans += answer


print(ans)