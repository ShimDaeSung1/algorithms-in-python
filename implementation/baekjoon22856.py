import sys
# readline()에는 마지막에 enter가 들어가므로 strip
input = lambda: sys.stdin.readline().rstrip()
# 재귀를 사용해아하면 필수, 파이썬의 기본 재귀 깊이 제한이 1000으로 매우 얕기 때문
sys.setrecursionlimit(10**6)



#Tree를 먼저 중위순회 해보고 마지막에 방문하는 정점이 어디인지 파악한다.
#전체 간선의 개수의 두배에서 마지막에 방문하는 정점을 방문하기 위해 지나온 간선의 개수를
#빼주어서 출력하면 끝, (루트노드에서 오른쪽 노드의 이동 횟수를 뺌)

left = dict()
right = dict()

#노드의 개수 N
N = int(input())
#각 노드(인덱스)별 부모 표시, 노드는 0이 없기 때문에 N+1
parent = [0]*(N+1)
node_count = 0

for _ in range(N):
    a, b, c = map(int, input().split())
    left[a]=b
    right[a]=c

    if b != -1:
        parent[b] = a
        node_count += 1
    if c != -1:
        parent[c] = a
        node_count += 1
    
# 마지막 노드 구하기
last_node = 0
def traverse(node):
    global last_node
    if node == -1:
        return
    #중위 순회 이므로 왼쪽 호출 뒤 last_node에 node 저장, 그 후 오른쪽을 호출한다.
    traverse(left[node])
    last_node = node
    traverse(right[node])
#루트노드는 항상 1이다. 시작점
traverse(1)

edge_count = node_count*2
movement = 0
#마지막 노드까지 이동 경로의 거리 구하기
while last_node != 1:
    movement += 1
    last_node = parent[last_node]
print(edge_count - movement)






