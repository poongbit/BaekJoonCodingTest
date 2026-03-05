from collections import deque
import sys
input = sys.stdin.readline

"""

1. graph[a].append(b) : A(선행, now_node)가 완성되어야 B(후행, next_node)를 지을 수 있다. 즉, A가 완성될 때 B의 족쇄를 푼다

2. 해금: 큐 입장 조건
큐(q) 입장 프리패스 조건은 오직 하나, 내 앞길을 막는 족쇄가 모두 풀린 상태인 indegree == 0 뿐이다.

3. 시간 누적: 동시 건축
 SCV들은 동시에 건물을 올리므로,다음 건물의 최종 시간은,
 나를 찌르는 여러 선행 건물 중 '가장 늦게 끝나는 굼벵이 건물의 시간'을 기다려줘야 하므로 무조건 max로 덮어씌운다


"""






# 1. 입력받기 및 변수 선언

N = int(input()) # 건물 종류

building_time = [0] * (N+1) # 각각의 건물 번호를 짓기 위해 걸리는 시간
building_graph = [[] for _ in range(N+1)] # 건물을 짓기 위해 선행되어야 할 건물들을 담은 리스트
in_degree = [0] * (N+1) # 건물을 짓기 위해 필요한 진입 차수

result_time = [0] * (N+1) # 순서를 지키고 난 후 건물이 완성되는 시간을 담은 리스트

for i in range(1,N+1):
    building_info = list(map(int,input().split()))

    # 빌딩 건축을 위한 시간을 슬라이싱
    building_time[i] = building_info[0]

    index = 1 # building info를 탐색하기 위한 인덱스 변수 선언

    while building_info[index] != -1:
        pre_building = building_info[index] # 선행되어야 할 건물 정보 슬라이싱
        building_graph[pre_building].append(i) # pre_building이 지어져야 i 빌딩을 건축할 수 있음
        in_degree[i] +=1 # i 빌딩을 건축하기 위한 진입 차수가 +1
        index +=1 # 탐색을 위한 +1


# 2. 위상 정렬 함수 정의하기

def topology():

    # 큐 선언
    q = deque()

    # 최초의 시작 지점 설정
    
    for i in range(1,N+1):
        if in_degree[i] == 0: # 진입 차수가 0이면 바로 건축할 수 있음
            q.append(i)
            result_time[i] = building_time[i] 


    while q:
        now_node = q.popleft() # 현재 건물을 popleft

        for next_node in building_graph[now_node]: # 현재 빌딩 이후에 다음 빌딩들에 대하여
            
            in_degree[next_node] -= 1 # next_building이 나왔으므로 진입 차수 -1

            # 다음 건물이 지어지므로, 건물 지어진 시간 결과를 먼저 기록한다.
            # 기존에 걸리는 시간 vs 현재 지어진 건물 + 다음 건물 지어지는 건물 시간       
            result_time[next_node] = max(result_time[next_node],result_time[now_node] + building_time[next_node])

            if in_degree[next_node] == 0:
                q.append(next_node)



topology()

for i in range(1,N+1):
    print(result_time[i])
                




