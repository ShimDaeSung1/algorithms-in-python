import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)#기본적으로 반복은 1000회로 되어 있기 때문에 늘려줌

#노드의 개수
n = int(input())

#트리
tree = [[] for _ in range(n+1)]

#부모 노드 저장
parent = [0 for _ in range(n+1)]
parent[1] = 1
#트리 구조 입력
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

# DFS는 항상 부모노드부터 자식노드 방향으로 탐색
def dfs(root):
    for i in tree[root]:
        if parent[i] == 0:
            parent[i] = root
            dfs(i)

dfs(1)

for i in range(2, n+1):
    print(parent[i])




