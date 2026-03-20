import sys
input = sys.stdin.readline

n = int(input())

sentence = str(input().strip())

word = ''

for i in range(5,0,-1):
    word += sentence[-i]

print(word)