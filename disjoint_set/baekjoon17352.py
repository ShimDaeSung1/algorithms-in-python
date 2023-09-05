import sys
input = sys.stdin.readline

def get_parent(x):
    global parent

    if x == parent[x]:
        return parent[x]
    
    p = get_parent(parent[x])
    return p

def union(x, y):
    parent_x = get_parent(x)
    parent_y = get_parent(y)

    if parent_x > parent_y :
        parent[parent_x] = parent_y
    else:
        parent[parent_y] = parent_x

n = int(input())
lands = [list(map(int, input().split())) for _ in range(n-2)]
parent = [i for i in range(n+1)]

for x,y in lands:
    union(x,y)
    
answers = set()
for i in range(1,n+1):
    answers.add(get_parent(i))

print(*answers)
