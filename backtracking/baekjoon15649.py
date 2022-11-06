import sys
sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

n, m = map(int, input().split())
result = []
visited = [False]*(n+1)

def backTracking(depth):
    if depth == m:
        print(' '.join(map(str, result)))
        return
    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = True
            result.append(i)
            backTracking(depth+1)
            result.pop()
            visited[i] = False

backTracking(0)

