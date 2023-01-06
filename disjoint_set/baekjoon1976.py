import sys
input = sys.stdin.readline

# 도시의 수
n = int(input())
# 여행 계획에 속한 도시들의 수
m = int(input())

# 도시끼리 연결된 여부
graph = [list(map(int, input().split())) for _ in range(n)]

#여행 계획
travel_plan = list(map(int, input().split()))
# 부모 노드
parent = [i for i in range(n+1)]

def get_parent(x):
    global parent
    if parent[x] == x :
        return parent[x]
    
    parent[x] = get_parent(parent[x])
    return parent[x]

def union(x,y):
    global parent
    a = get_parent(x)
    b = get_parent(y)
    #a와 b의 부모를 각각 구한 후, 
    #더 작은 부모의 숫자로 합친다.

    if a>b :
        parent[a] = parent[b]
    else:
        parent[b] = parent[a]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            union(i+1, j+1)

answer = parent[travel_plan[0]]
for i in travel_plan:
    if parent[i] != answer:
        print("NO")
        exit()
print("YES")