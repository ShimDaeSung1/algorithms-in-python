import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
s = []

def backtracking(depth):
    if depth == m :
        print(' '.join(map(str, s)))
        return
    for i in range(n):
        s.append(arr[i])
        backtracking(depth+1)
        s.pop()
backtracking(0)
