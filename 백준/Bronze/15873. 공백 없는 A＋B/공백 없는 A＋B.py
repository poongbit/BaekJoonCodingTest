import sys

input = sys.stdin.readline

number = str(input()).strip('\n')

length = len(number)


if number[-2:] == '10':
    left_number = number[:-2]

    print(int(left_number) + 10)

else:
    left_number = number[:-1]
    right_number = number[-1]

    print(int(left_number) + int(right_number))