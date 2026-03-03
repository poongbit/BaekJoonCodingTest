"""
[백준 2251 - 물통] 실전 압축 3줄 요약
1. [상태가 노드다] 방 번호가 없어도 당황하지 말 것! "물통 A, B에 든 물의 양(a, b)" 그 자체가 하나의 방(Node) 좌표가 되며, 이를 위해 visited[a][b] 2차원 출석부를 만든다.

2. [반복되는 6가지 행동] "A→B, B→C..." 같은 6가지 물 붓기 노가다는 moves 리스트로 미리 정의해두고, for sender, receiver in moves: 반복문 하나로 우아하게 처리한다.

3. [물 붓기의 수학적 공식] 옮길 수 있는 물의 양(water)은 '주는 놈의 잔량'과 '받는 놈의 빈 공간' 중 더 작은 값(min)이며, 계산 후에는 반드시 새로운 상태를 큐에 넣어 파도를 이어간다.

"""



from collections import deque
import sys

input = sys.stdin.readline

A,B,C = map(int,input().split())

# A,B 정보만 알면, C 방문은 알아서 아는 것과 마찬가지다.

visited = [[False] * 201 for _ in range(201)]

# 엣지가 주어진게 아니라, 상태로 존재하기 때문에 따로 sender, receiver로 정한다
# a,b,c의 인덱스를 0,1,2로 설정하고, (sender, receiver)로 정한다
moves = [(0,0),(0,1),(0,2),(1,0),(1,2),(2,0),(2,1)]

answer = [] # A 물통의 물이 0 일때, C의 물통 속 물을 담는 공간


def BFS():
    queue = deque()
    # 초기의 a,b는 텅텅 비어 있으므로 (0,0), a,b,c는 각 통에 있는 물의 양 상태
    queue.append((0,0))

    visited[0][0] = True # (a=0,b=0)일때의 값이 존재함

    while queue:
        # 1. 꺼낸다
        a,b = queue.popleft()

        c = C - a - b # a와 b를 알 때, c는 자동으로 정해진다.

        # 2. 정답 조건이 맞는지 확인한다

        if a == 0:
            answer.append(c)

        for sender, receiver in moves:
            now = [a,b,c]
            limit = [A,B,C]

            # 이동하게 될 물의 양 계산

            current_sender = now[sender]
            current_receiver = now[receiver]

            receiver_capacity = limit[receiver]
            
            # 이동하게 될 물의 양은 (보내는 물의 양)과 (받는 물통의 수용량에서 받는 물의 양)을 뺀 값 중에서 작은 것이 된다.
            left_water = min(current_sender, receiver_capacity - current_receiver)

            # 보내고 난 후의 물의 양 업데이트
            now[sender] -= left_water
            now[receiver] += left_water


            # 이후에 새로운 a,b로 갱신하기

            new_a = now[0]
            new_b = now[1]

            # 새로운 a,b에 대해서 visited 체크 여부 확인

            if not visited[new_a][new_b]:
                visited[new_a][new_b] = True
                queue.append((new_a,new_b)) #.새로 갱신된 a,b로 큐에 넣어서 파문을 일으킴


BFS()

answer.sort()

for ans in answer:
    print(ans, end= " ")

