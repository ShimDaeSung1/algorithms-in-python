import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m  = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
s = []
visited = [False]*(len(numbers))
def dfs(depth):
    if depth == m:
        print(' '.join(map(str, s)))
        return
    for i in range(len(numbers)):
        if visited[i] == False:
            visited[i] = True
            s.append(numbers[i])
            dfs(depth+1)
            visited[i] = False
            s.pop()
dfs(0)


