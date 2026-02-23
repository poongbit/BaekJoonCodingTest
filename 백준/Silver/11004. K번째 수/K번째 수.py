import sys
input = sys.stdin.readline
N,K = map(int,input().split()) # 데이터의 개수, K번째에 있는 수

A = list(map(int,input().split())) # 배열 입력 받기


def quickSort(S,E,K): # Start,End,Kth
    global A
    if S < E:
        
        # 분할로 구역 나누기
        pivot = partition(S,E) # 반환값은 j의 인덱스
        
        if pivot == K: # K번째 수가 pivot이면 더는 구할 필요 없음
            return

        elif K < pivot: # K가 pivot보다 작으면 왼쪽 그룹만 정렬
            quickSort(S, pivot - 1, K)

        else:
            quickSort(pivot + 1, E, K)



def swap(i,j):
    global A
    temp = A[i]
    A[i] = A[j]
    A[j] = temp


def partition(S,E): # 분할 정렬
    global A

    if S + 1 == E: # 시작점 옆에 끝 점이 있을 때
        if A[S] > A[E]: # 시작점 위치의 데이터가 더 클 경우
            swap(S,E) # 스왑한다
        
        return E # 끝 지점을 반환하여 이 값이 새 pivot이 된다.


    M = (S + E) // 2 # 중앙값 선언
    swap(S,M) # 중앙값을 시작 위치와 swap

    pivot = A[S] # pivot을 시작 위치 값 A[S]로 저장한다.

    # 순찰할 시작과 끝을 선언한다.
    i = S + 1
    j = E

    while i <= j: # 엇갈리면 검사가 끝남
        while pivot < A[j] and j > 0: # 피봇값보다 작은 데이터를 찾을 떄까지 왼 쪽으로 이동
            j = j - 1

        while pivot > A[i] and i < len(A) - 1: # 피봇값보다 큰 값을 찾을 떄 까지 오른쪽으로 이동
            i = i + 1

        if i <= j:
            swap(i,j)
            i = i+1
            j = j - 1

    
    # 엇갈린 후에, j에 위치한 데이터는 pivot값보다 작음

    A[S] = A[j] # 경계선에 있던 작은 데이터를 맨 앞으로 보내주고
    A[j] = pivot # 대기석에 숨겨놨던 피벗을 다시 제자리에 둠
    
    return j # 피벗이 최종적으로 안착한 위치를 반환함.

quickSort(0, N-1, K-1)

print(A[K-1])