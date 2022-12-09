import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
# 0~n까지 각각 n+1 개의 집합, m개의 연산
n, m = map(int, input().split())
# parent[0] = 0, 자기자신으로 부모 초기화
parent = [i for i in range(n+1)] 

def get_parent(x):
    # 부모가 같아지면 더이상 부모가 없으므로 자기자신 리턴
    if parent[x] == x : return x
    # 가장 상위부모까지 올라가서 찾음
    parent[x] = get_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    parent_a = get_parent(a)
    parent_b = get_parent(b)

    # 부모끼리 합치는데, 더 작은 숫자의 부모가 큰 숫자의 부모가 된다.
    if parent_a > parent_b : 
        parent[parent_a] = parent_b
    else:
        parent[parent_b] = parent_a
answer = []
for i in range(m):
    uf, a, b = map(int, input().split())
    # 0일경우 집합을 합친다.
    if uf == 0:
        union_parent(a, b)
    else:
        if get_parent(a) == get_parent(b):
            answer.append("YES")
        else:
            answer.append("NO")
for i in answer:
    print(i)