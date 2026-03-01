import sys

n = sys.stdin.readline()

sequence = n.split('-')

result = sum(map(int,sequence[0].split('+')))


for i in range(1,len(sequence)):
    # 각 그룹에서 내부의 덧셈을 처리하고 결과를 빼기기
    second_sequence = sum(map(int,sequence[i].split('+')))

    result -= second_sequence


print(result)
    