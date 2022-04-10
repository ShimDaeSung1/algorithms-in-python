import sys
input = sys.stdin.readline

N = int(input())
for i in range(N):
    M = int(input())
    arr = list(map(int, input().split()))
    print(min(arr), max(arr))
