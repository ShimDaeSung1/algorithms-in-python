import sys
input = sys.stdin.readline

def get_parent(x):
    global parent
    # 부모가 없다면 최상위, 자신을 리턴
    if parent[x] == x : 
        return x
    
    parent[x] = get_parent(parent[x])
    return parent[x]        

def union_parent(a,b):
    global know_list, parent
    parent_a = get_parent(a)
    parent_b = get_parent(b)
    
    if parent_a in know_list:
        parent[parent_b] = parent_a
    elif parent_b in know_list:
        parent[parent_a] = parent_b
    else:
        if parent_a < parent_b:
            parent[parent_b] = parent_a
        else:
            parent[parent_a] = parent_b

# 사람의 수, 파티의 수
n,m = map(int, input().split())
parent = [i for i in range(n+1)]

# 진실을 아는 사람의 수와 번호
know_list = list(map(int, input().split()))[1:]

party_list = [[] for _ in range(m)]

# 각 파티에 오는 사람들 
for i in range(m):
    party_list[i] = list(map(int, input().split()))[1:]

# 어떤 사람이 어떤 파티에서는 진실을 듣고, 또다른 파티에서는 과장된 이야기를 들었을 때도 지민이는 거짓말쟁이로 알려지게 된다.
# => 이미 진실을 들은 경우에는 피해야함. 즉 돌면서 진실을 말했던 사람의 경우에 같이 엮어줘야함
answer = 0

# 파티 리스트를 돌면서 진실의 집합을 묶어준다.
for list in party_list:
    for i in range(1, len(list)):
        union_parent(list[i], list[i-1])

for list in party_list:
    for i in list:
        # 진실을 아는 집단일 경우
        if get_parent(i) in know_list:
            break
    else:
        answer += 1
print(answer)
