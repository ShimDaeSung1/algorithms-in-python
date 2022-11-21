import sys
input = sys.stdin.readline

def dfs(start,cur,value,visited):
    global min_value

    if len(visited) == n:
        if to_city[cur][start] >= 1:
            min_value = min(min_value, value + to_city[cur][start])
        return
    
    for i in range(n):
        if to_city[cur][i] >= 1 and i not in visited and value < min_value:
            visited.append(i)
            dfs(start, i, value+to_city[cur][i], visited)
            visited.pop()

n = int(input())
to_city = [list(map(int, input().split())) for _ in range(n)]
visited = [False]*n
min_value = float("inf")

for i in range(n):
    dfs(i,i,0,[i])

print(min_value)

