import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
s = []

def dfs(start):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(start, n+1):
        s.append(i)
        dfs(i)
        s.pop()
dfs(1)

    