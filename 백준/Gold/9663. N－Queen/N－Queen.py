# 문제 27 : N - queen 배치하기

"""

N : 체스판 크기 N * N
cnt : 퀸을 배치하는 경우의 수 저장 변수


cols : 열 충돌 여부 저장 리스트
diag1 : 오른쪽 위 대각선 충돌 여부 리스트, row + col
diag2 : 오른쪽 아래 대각선 충돌 여부 리스트, row - col + N -1 (인덱스가 음수가 되지 않도록 더함)
백 트래킹 실행 (매개 변수 : 현재 행)

# 백트래킹 상세 구현

backtrack(현재 행):
    # 1. 종료 조건
    if 현재 행 == N:
        cnt +=1 # 경우의 수 증가
        함수 종료

    # 2. DFS, 백트래킹

    for (0부터 N-1까지 열 반복):
        if (현재 열, 오른쪽 위 대각선, 오른쪽 아래 대각선 모두 사용이 안된 경우):
            열, 오른쪽 위 대각선, 오른쪽 아래 대각선 사용 표시
            backtrack(현재행 + 1)
            열, 오른쪽 위 대각선, 오른쪽 아래 대각선 사용 취소 # 롤백


backtrack(0) 실행
print(cnt) 출력

"""

import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)


N = int(input())
cnt = 0

# 퀸의 공격 반경을 기록할 3개의 '통제 구역' 체크리스트
cols = [False] * N #열 충돌 체크
diag1 = [False] * (2 * N -1) # 오른쪽 위 대각선 충돌 체크, (row + col이 같으면 같은 선상)
diag2 = [False] * (2 * N -1) # 오른쪽 아래 대각선 충돌 체크, (row - col이 같으면 같은 선상)


def backtrack(row):
    global cnt

    if row == N: # N행에 다 배치가 된거면 성공
        cnt += 1 # 경우의 수 증가
        return  # 함수 종료

    for col in range(N): # 열 기준으로 둘 자리 탐색
        if not cols[col] and not diag1[row+ col] and not diag2[row -col + N-1]:
            cols[col] = diag1[row + col] = diag2[row-col + N - 1] = True
            backtrack(row + 1) # 다음 행으로 넘어감
            cols[col] = diag1[row + col] = diag2[row -col + N - 1] = False

backtrack(0)
print(cnt)