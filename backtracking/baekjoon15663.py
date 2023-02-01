import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
answers = set()
visited = [False]*(n)
s = []

def backtracking(depth):
    if depth == m :
        # set에 추가시 튜플로 변경
        answers.add(tuple(s))
        return

    for i in range(n):
        if visited[i] == False:
            visited[i] = True
            s.append(arr[i])
            backtracking(depth+1)
            s.pop()
            visited[i] = False

backtracking(0)
for i in sorted(answers):
    print(*i)


