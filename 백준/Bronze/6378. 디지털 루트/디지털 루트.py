import sys

input = sys.stdin.readline



# 1. 입력값 받기


"""
## 안쪽부터 차근차근 분해하기


```
num = 123
       ↓ str()
     "123"
       ↓ map(int, ...)
     1, 2, 3
       ↓ list()
     [1, 2, 3]
       ↓ sum()
       6
```

숫자의 각 자릿수 합을 구한다


"""


while True:

    number = int(input())

    if number == 0:
        break


    while True:

        number = sum(list(map(int,str(number))))


        if number // 10 == 0: # 10으로 안 나누어 떨어질 때까지
            print(number)
            break