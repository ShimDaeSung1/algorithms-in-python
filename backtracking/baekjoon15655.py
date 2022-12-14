import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 이 문제는 조합(C) 문제

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
s = []

def backtracking(start):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(start, n):
        s.append(arr[i])
        backtracking(i+1)
        s.pop()
backtracking(0)



