import sys
input = sys.stdin.readline
from itertools import combinations

"""
L : 서로 다른 L개의 알파벳 소문자들로 구성
최소 한 개의 모음(aeiou), 최소 두 개의 자음

암호에서 증가하는 순서로 배열

C : 조교들이 암호로 사용했을 법한 문자의 종류 가지
C개의 문자들이 주어짐, 

가능성있는 암호들을 모두 구하는 프로그램

"""
L,C = map(int,input().split())

letter_list = list(map(str,input().split()))

# 모음
vowels = ['a','e','i','o','u']

letter_list.sort()

answer = []

def DFS(start,path):
    if len(path) == L:
        # 모음 1개 이상 여부 확인
        v_count = 0
        c_count = 0

        for item in path:
            if item in vowels:
                v_count +=1

            else:
                c_count +=1


        if c_count >=2 and v_count>=1:
            print(''.join(path))
        

    for i in range(start,C):
        DFS(i+1,path + [letter_list[i]])


DFS(0,[])