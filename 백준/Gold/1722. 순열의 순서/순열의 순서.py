# 백준 1722번 - 순열의 순서 구하기

"""

1. 인덱스 = Offset (내 앞에 버려진 개수)

# index = '시작점으로부터 건너뛴 칸 수' (0-based)
# "K번째" → index = K-1  /  array[i] → i칸 건너뜀


---

2. 순서 중요 → 순열(n!), 순서 무관 → 조합(DP/파스칼)

# [1,2] ≠ [2,1] : 순열 → factorial 사용
# [1,2] == [2,1] : 조합 → DP (파스칼의 삼각형) 사용



3. N! 같은 거대한 수 → while 루프 금지, 몫//·나머지% 로 점프

# 큰 순열에서 K번째 원소 찾기 → 브루트포스 X
# (K-1) // (n-1)! → 몇 번째 묶음인지
# (K-1) %  (n-1)! → 묶음 내 나머지 위치
# O(N)으로 해결, 절대 O(N!) 루프 돌리지 말 것



"""

import sys
input = sys.stdin.readline

N = int(input())

# 입력값을 일단 통째로 리스트로 받는다.
query = list(map(int,input().split()))

# 팩토리얼 저장 배열 생성
fact = [1] * (N+1)
for i in range(1,N+1):
    fact[i] = fact[i-1] * i

nums = [i for i in range(1,N+1)]

if query[0] == 1:
    # 1번 문제일 떄만 K를 가져온다
    K = query[1]

    K-=1 # 0-based 인덱스 맞추기
    
    ans = []

    # 남은 자릿수(N-1)부터 0까지 거꾸로 내려간다.
    for i in range(N-1,-1,-1):
        idx = K // fact[i]
        ans.append(nums.pop(idx))
        K %= fact[i]

    print(*ans) # 리스트 안의 요소들을 띄어쓰기로 예쁘게 출력

elif query[0] == 2:
    # 소문제 2번 로직

    # 체크해야 하는 순열
    check_nums = query[1:]
    count = 0


    for i in range(N):
        # 이번에 확인해야 할 숫자
        current_num = check_nums[i]

        # current_num이 nums에서 어디 index를 차지하는 지 찾기
        # index값은 자기보다 앞에 있는 값이 몇 개 인지를 반환함
        idx = nums.index(current_num)

        # 내 앞에 버려진 개수 구하기
        count += idx * fact[N-1-i]

        # 다 썻으면 버리기
        nums.pop(idx)


    # 내 앞에 count개 있으므로, 내 차례는 count + 1
    print(count + 1)



