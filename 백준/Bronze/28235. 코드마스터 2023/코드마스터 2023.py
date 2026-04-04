import sys
input = sys.stdin.readline
from collections import defaultdict

name = str(input().strip())


word = defaultdict(str)

word['SONGDO'] = 'HIGHSCHOOL'
word['CODE'] = 'MASTER'
word['2023'] = '0611'
word['ALGORITHM'] = 'CONTEST'

print(word[name])