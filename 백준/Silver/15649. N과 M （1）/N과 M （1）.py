# 문제 26 N과 M

"""
N,M : 1부터 N까지 자연수를 선택하여 길이가 M인 수열 모두 구함
visited : 숫자 사용 여부 저장 리스트
S : 수열 정보 저장 리스트


# 백트래킹 상세 구현하기
backtrack(수열 길이):
    if 길이가 M인 수열이 만들어진 경우:
        수열 정보 출력 (단, 인덱스 + 1하여 출력) 후 함수 종료

    for (0부터 N-1까지 탐색): # i를 수열에 넣으면 실제 수는 i+1

        if (아직 수열에 포함되지 않은 수인 경우):
            visited[i] = True # 수 사용을 표시
            S[length] = i # 수열에 수 저장
            backtrack(length + 1) # 다음 위치로 이동
            visited[i] = False # 수 사용 취소(백 트래킹)


백트래킹 실행(0)

"""

import sys
input = sys.stdin.readline

N,M = map(int,input().split())
S = [0] * M  # 수열을 저장할 리스트
visited = [False] * N # 숫자 사용 여부 저장 리스트

def backtrack(length):
    if length == M: # 길이가 M인 수열이 만들어진 경우
        print(' '.join(str(x + 1) for x in S)) # 아래에 인덱스로 0~ n-1까지 했으므로, 실제는 +1을 해줘야 함
        return

    for i in range(N): # 0 ~ n-1까지
        if not visited[i]:
            visited[i] = True
            S[length] = i # length 인덱스 위치에 숫자를 기록함
            backtrack(length + 1) # 다음 길이로 추가로 탐색
            visited[i] = False # 백트래킹 (수 반납)


backtrack(0)