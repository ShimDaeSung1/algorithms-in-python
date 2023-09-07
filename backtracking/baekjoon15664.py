import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr = sorted(arr)
s = []
answers = set()

def backtracking(start):
    if len(s) == m:
        # answer = ' '.join(map(str, s))
        answers.add(tuple(s))
        return
    for i in range(start, n):
        s.append(arr[i])
        backtracking(i+1)
        s.pop()
backtracking(0)
for i in sorted(answers):
    print(*i)

