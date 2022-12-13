import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

#사람의 수, 친구 관계의 수
n, m = map(int, input().split())

graph = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

def dfs(node, cnt):
    if cnt == 5:
        print(1)
        exit()
    
    for i in range(n):
        if graph[node][i] == 1:
            cnt+=1
            dfs(i, cnt)
            cnt-=1

for i in range(n):
    dfs(i, 1)
print(0)


    
    
