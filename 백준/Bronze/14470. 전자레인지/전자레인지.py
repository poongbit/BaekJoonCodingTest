import sys
input = sys.stdin.readline

origin_temp = int(input())
target_temp = int(input())
frozen_heat_time = int(input())    # 얼음 구간 1도당 시간
frozen_solving_time = int(input()) # 0도 해동 시간
heating_time = int(input())        # 일반 구간 1도당 시간


count = 0

if origin_temp < 0:
    # 구간 1: 음수 → 0 (얼음 해동 구간)
    count += (-origin_temp) * frozen_heat_time
    # 구간 2: 0도 해동
    count += frozen_solving_time
    # 구간 3: 0 → target (일반 가열 구간)
    count += target_temp * heating_time
else:
    # 구간 3만: origin → target (일반 가열 구간)
    count += (target_temp - origin_temp) * heating_time

print(count)