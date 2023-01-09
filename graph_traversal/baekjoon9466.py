import sys
input = sys.stdin.readline

def dfs(visited, stack, x):

    if want[x] in stack:
        if want[x] == x:
            return
        for i in stack:
            visited[i] = True
        return
    
    stack.append(want[x])
    dfs(visited, stack, want[x])



T = int(input())

for _ in range(T):
    #학생 수
    n = int(input())
    want = list(map(int, input().split()))
    want.insert(0,0)

    visited = [False for _ in range(n+1)]
    for i in range(1,n+1):
        if visited[i] == False:
            if want[i] == i: 
                visited[i] = True
                continue
            stack = [i]
            dfs(visited, stack, i)
    print(visited.count(False)-1)

    



