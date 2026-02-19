# 문제 9 DNA 비밀번호


import sys
input = sys.stdin.readline


check_list = [0] * 4 # 목표치, A,C,G,T가 최소 각각 몇 개 있어야 하는 지
my_list = [0] * 4 # 내가 보고 있는 부분 문자열 안에 A,C,G,T가 몇 개가 있는 지
check_num = 0# A,C,G,T 중에 조건을 만족하는 알파벳의 개수


# 함수 정의


def myadd(c): # 새로 들어온 문자를 처리하는 함수
    # 바깥에 선언된 변수들을 이용하겠다
    global check_list, my_list, check_num

    if c == 'A':
        my_list[0] +=1
        if check_list[0] == my_list[0]: # 이미 달성도를 올려줬기 때문에 >= 하게 되면 또 올라감
            check_num +=1

    elif c == 'C':
        my_list[1] +=1
        if check_list[1] == my_list[1]:
            check_num +=1

    elif c == 'G':
        my_list[2] +=1
        if check_list[2] == my_list[2]:
            check_num +=1

    elif c == 'T':
        my_list[3] +=1
        if check_list[3] == my_list[3]:
            check_num +=1


def myremove(c):    # 제거되는 문자를 처리하는 함수
    global my_list, check_list, check_num

    if c == 'A':
        if check_list[0] == my_list[0]: # 제거되므로 달성도는 한 번 빠짐
            check_num -=1
        # 알파벳 개수도 빠짐
        my_list[0] -=1

    elif c == 'C':
        if check_list[1] == my_list[1]:
            check_num -=1

        my_list[1] -=1


    elif c == 'G':
        if check_list[2] == my_list[2]:
            check_num -=1

        my_list[2] -=1


    elif c == 'T':
        if check_list[3] == my_list[3]:
            check_num -=1

        my_list[3] -=1


# 문자열의 길이, 부분 문자열의 길이
S,P = map(int,input().split())


# DNA 문자열
A = list(input())

# 부분 문자열에 포함되어야 할 A,C,G,T의 최소 개수
check_list = list(map(int,input().split()))

# 가능한 비밀 번호 가짓수 초기화
result = 0


# 어느 문자가 0개이면 이미 만족한 것과 마찬가지므로, check_num을 늘려주기

for i in range(4):
    if check_list[i] == 0:
        check_num +=1


# 초기 P 부분 문자열 처리 부분

for i in range(P):
    myadd(A[i])


# 이미 여기서 부터 4 종류 문자의 개수 조건을 모두 충족시킨 경우
if check_num == 4:
    result +=1




for i in range(P,S): # 부분 문자열에서, 전체 문자열 사이, 슬라이딩 윈도우 핵심
   
    j = i - P  # 창문의 왼쪽 끝 인덱스 선언

    myadd(A[i]) # I: 창문의 오른쪽 인덱스, 추가되면서 문자가 새로 들어옴
    myremove(A[j]) # J : 창문의 왼쪽 끝 인덱스, 이동하면서 빠져나감

    if check_num == 4: # 한 부분 문자열 구간 안에서, 이 조건을 만족하면, result 값 증가
        result +=1



# 결과값 도출

print(result)
    


