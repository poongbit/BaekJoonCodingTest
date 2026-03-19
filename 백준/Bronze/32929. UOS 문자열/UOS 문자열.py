import sys
input = sys.stdin.readline

x = int(input().strip())


word = 'UOS'

index =  x % (len(word))

print(word[index-1])