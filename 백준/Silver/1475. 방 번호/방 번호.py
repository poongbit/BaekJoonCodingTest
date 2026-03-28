import sys
from collections import defaultdict
import math

input = sys.stdin.readline

number = str(input().strip())

number_set = [i for i in range(0,10)]

# 숫자 개수 세기

number_dict = defaultdict(int)

for i in range(len(number)):

    if number[i] == '9' or number[i] == '6':
        number_dict['9'] +=1

    else:


        number_dict[number[i]] +=1


result = sorted(number_dict.items(),key = lambda x : -x[1])


ans = 0

for key, val in number_dict.items():
    if key == '9' or key == '6':
        ans = max(ans,math.ceil(val/2))

    else:
        ans = max(ans,val)





print(ans)

