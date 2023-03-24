from sys import stdin

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    
    if a in people:
        parent[b] = a
    elif b in people:
        parent[a] = b
    else:
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

N, M = map(int, stdin.readline().split())
people = list(map(int, stdin.readline().split()))[1:]
party = []
parent = list(range(N+1))
answer = 0

for m in range(M):
    n = list(map(int, stdin.readline().split()))
    p = n[1:]
    for i in range(n[0]-1):
          union(p[i], p[i+1])
    party.append(p)
    
for i in range(len(party)):
    for j in range(len(party[i])):
          if find(party[i][j]) in people:
                break
    else:
      answer += 1

print(answer)
