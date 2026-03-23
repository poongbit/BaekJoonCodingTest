import sys
input = sys.stdin.readline

case = 0

while True:
    number = int(input().strip())

    if number == 0:
        break

    else:
        num_1 = number * 3

        if num_1 % 2 == 0:
            num2 = num_1 // 2

        else:
            num2 = (num_1+1) // 2

        
        n3 = 3 * num2

        n4 = n3 // 9

    if num_1 % 2 == 0:
        result = 2*n4

    else:
        result = 2*n4 + 1

    
    if number % 2 != 0:
        case +=1
        print(f'{case}. odd {n4}')

    else:
        case +=1
        print(f'{case}. even {n4}')


