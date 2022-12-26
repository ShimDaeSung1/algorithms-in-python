import sys
input = sys.stdin.readline

#학생 수, 친구 관계 수, 가지고 있는 돈
n, m, k = map(int, input().split())
# 각각 학생이 원하는 돈
require_money = list(map(int, input().split()))
require_money.insert(0, 0)

parent = [i for i in range(n+1)]

def get_parent(x):
    global parent
    if parent[x] == x:
        return x
    
    parent[x] = get_parent(parent[x])
    return parent[x]

def union_parent(x,y):
    a = get_parent(x)
    b = get_parent(y)

    if a>b:
        parent[a] = b
    else:
        parent[b] = a

for i in range(m):
    a, b = map(int, input().split())
    union_parent(a,b)

#부모가 1~n까지의 비용
cost = [0]*(n+1)

for i in range(1,n+1):
    # 현재 학생의 부모집합
    p = get_parent(i)
    money = require_money[i]

    if cost[p] == 0:
        cost[p] = money
    else:
        cost[p] = min(cost[p], money)

if sum(cost[1:n+1]) > k :
    print("Oh no")
else:
    print(sum(cost[1:n+1]))

