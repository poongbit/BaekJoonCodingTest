import sys
input = sys.stdin.readline

n = int(input().strip())
from collections import defaultdict

number_list = []

for _ in range(n):
    a = int(input().strip())
    number_list.append(a)


# 1. 산술 평균
sum = 0
for item in number_list:
    sum += item


print(round(sum/len(number_list)))

# 2. 중앙값

number_list.sort()

index = len(number_list) // 2

print(number_list[index])


# 3. 최빈값
number_dict = defaultdict(int)

for item in number_list:
    number_dict[item] +=1


result = sorted(number_dict.items(),key = lambda x : (-x[1],x[0]))

# 최빈값이 같은 것들만을 추리기
max_freq = result[0][1]
modes = []

for k,v in result:
    if v == max_freq:
        modes.append(k)


if len(modes) >=2:
    print(modes[1])

else:
    print(modes[0])


# 4. 범위

print(number_list[-1]-number_list[0])