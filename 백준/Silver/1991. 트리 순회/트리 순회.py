# 백준 1991번

# 입력 받기 
import sys
input = sys.stdin.readline

N = int(input().strip())

# 1. 텅 빈 딕셔너리 트리 생성
tree = {}

# 2. 트리 조합하기 (입력 파싱)
for _ in range(N):
    # 알파벳 3개가 띄어쓰기로 들어오니 split()으로 이쁘게 찢는다.
    node, left, right = input().split()


    # 딕셔너리에 '부모 = (왼쪽 자식, 오른쪽 자식)' 형태로 저장!
    tree[node] = (left,right)


# 순회 탐색 함수 만들기

# 전위 순회 (나 -> 왼쪽 -> 오른쪽)
def preorder(node):
    if node != '.': # 자식 노드가 있다면
        print(node,end= "") # 내 도장을 먼저 쾅 찍기
        preorder(tree[node][0]) # 왼쪽 자식으로 직진
        preorder(tree[node][1]) # 오른쪽 자식으로 직진
        pass

# 중위 순회 (왼쪽 -> 나 -> 오른쪽)
def inorder(node):
    if node !='.':
        inorder(tree[node][0]) # 왼쪽 자식부터 일 먼저 시킨다
        print(node,end = '')
        inorder(tree[node][1]) #오른쪽 자식 일 시킨다.
        pass

# 후위 순회 (왼쪽 -> 오른쪽 -> 나)
def postorder(node):
    if node != '.':
        postorder(tree[node][0])
        postorder(tree[node][1])
        print(node,end = '')
        pass


##########

preorder('A')
print() # 줄바꿈
inorder('A')
print()
postorder('A')
