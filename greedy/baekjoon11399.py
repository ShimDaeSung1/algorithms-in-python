import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
sum = 0
arr.sort(reverse=True)
#
#43321
for i in range(0, N):
    for j in range(i, N):
        sum += arr[j]
print(sum)