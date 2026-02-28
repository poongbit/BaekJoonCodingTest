# 문제 21 버블 정렬 프로그램 2 1571번

"""
병합 정렬(s,e):
    s(시작점), e(종료점), m(중간점)

    # 재귀 함수 형태로 구현
    병합 정렬(s,m)
    병합 정렬(m+1,e)

    for s ~ e:
        tmp 리스트 저장

    # 두 그룹을 병합하는 로직
    index1 -> 앞쪽 그룹 시작점
    index2 -> 뒤쪽 그룹 시작점

    while index1 <= 중간점 and index2 <= 종료점:
        양쪽 그룹의 index가 가리키는 값을 비교한 후 더 작은 수를 선택해 리스트에 저장
        선택된 데이터의 index값을 오른쪽으로 한 칸 이동
        
        로직을 수행하면서 뒤쪽 데이터값이 더 작아 선택할 때
        swap이 일어난 것과 동일한 것이기 때문에
        현재 남은 앞쪽 그룹 데이터의 개수만큼 결괏값에 더함

    반복문이 끝난 후 남아 있는 데이터 정리


N(정렬할 수 개수)
A(정렬할 리스트 선언)
tmp(정렬할 때 잠시 사용할 임시 리스트 선언)

A 리스트에 데이터 저장하기 
병합 정렬 함수 수행
결괏값 출력


"""

import sys
input = sys.stdin.readline
result = 0


def merge_sort(s,e):
    global result
    
    if e - s < 1:
        return

    m = int(s + (e-s)/2)

    merge_sort(s,m) # 재귀 함수 형태로 구현
    merge_sort(m+1, e)

    for i in range(s, e+1):
        tmp[i] = A[i]

    k = s

    index1 = s
    index2 = m + 1

    while index1 <= m and index2 <= e: # 두 그룹을 병합하는 로직
        if tmp[index1] > tmp[index2]:
            A[k] = tmp[index2]
            
            result = result + index2 - k # 뒤쪽 데이터값이 더 작다면 결괏값 업데이트

            k +=1
            index2 +=1

        else:
            A[k] = tmp[index1]
            k += 1
            index1 +=1

    while index1 <=m:
        A[k] = tmp[index1]
        k +=1
        index1 +=1

    while index2 <=e:
        A[k] = tmp[index2]
        k +=1
        index2 +=1



N = int(input())
A = list(map(int,input().split()))

tmp = [0] * N

merge_sort(0,N-1)
print(result)