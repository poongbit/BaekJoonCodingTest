# 백준 1256번 - 사전 찾기

"""

1. 흐름 제어 — 독립 `if` 남발 금지

# 조건이 상호 배타적이면 if-elif-else 로 묶을 것
# 독립 if 연달아 쓰면 한 턴에 조건 여러 개가 동시에 발동 → 변수 이중 차감 버그
# 예외 처리 후 continue 로 즉시 다음 턴 점프하는 습관


2. 방어적 코딩 — 예외(0, 음수) 처리가 계산보다 무조건 먼저

# N=0 인데 dp[N-1] 접근 → index -1 (리스트 맨 뒤) 조용한 논리 버그 발생
# 인덱스에 빼기 연산이 들어가면 → 로직 맨 위에서 if N == 0: 방어막 먼저
# 순서: 예외 처리 → 메인 로직


3. 변수 갱신 — 루프 안에서 바뀌는 값은 매 턴 새로 계산

# 루프 바깥에서 한 번만 계산한 값 → 루프 안에서 N이 바뀌면 즉시 무효
# while 매 턴마다 "N이 바뀌었나?" 확인 후 의존 변수 전부 재계산
# 변수 생명 주기: 루프 밖(고정값) vs 루프 안(매 턴 갱신값) 구분 필수


"""

import sys
input = sys.stdin.readline

# 1. 입력 받기 및 변수 선언
N,M,K = map(int,input().split())

# N+M개 중 N개를 선택하기 위한 dp 배열 생성

dp = [[0] *(N+M+1) for _ in range(N+M+1)]

for i in range(N+M+1):
    dp[i][0] = 1
    dp[i][i] = 1


for i in range(2,N+M+1):
    for j in range(1,i):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]


# 맨 앞에 a를 선택한 것을 기준으로 경우의 수를 찾아감


# K가 전체의 경우의 수보다 클 경우
if K > dp[N+M][M]:
    print(-1)
    exit()

result = []

while N>0 or M>0:

    # 재고 소진 여부부터 확인한다.
    if N==0: # a가 다 떨어진 경우
        result.append('z')
        M -=1
        continue # 다 처리했으면 다음으로 넘어가라

    elif M==0:# z가 다 떨어진 경우
        result.append('a')
        N -=1
        continue

    a_block = dp[N-1+M][M] # 맨 앞에 a를 고정했을 때, 남은 'a'(N-1)개와 남은 'z'(M)개를 섞어서 고르는 경우의 수
        
    if K <= a_block: # K가 a 상자 안에 들어있을 경우
        result.append('a')
        N -=1

    else: # K가 a 상자 밖에 있는 경우
        result.append('z')
        M -=1
        K -= a_block # 'z'를 선택하기 위해 a_block 만큼 다 지나침


for item in result:
    print(item,end='')

