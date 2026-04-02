import sys
input = sys.stdin.readline

"""
로프를 병렬로 연결하면 중량을 나눌 수 있음
k개의 로프 활용, 중량이 w인 물체 들어올리기

각각 로프에는 모두 고르게 w/k만큼 중량이 걸림



"""

N = int(input().strip())

# 각 로프가 버틸 수 있는 최대 중량을 가진 리스트
rope = []

for index in range(N):
    weight = int(input().strip())
    rope.append((weight,index))

rope.sort(key=lambda x: x[0],reverse= True)

new_weight = 0


for i in range(len(rope)):
    new_weight = max(new_weight, rope[i][0] * (i+1))

print(int(new_weight))