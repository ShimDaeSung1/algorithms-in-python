import sys
input = sys.stdin.readline

#레벨의 수
N = int(input())
arr = []
for i in range(N):
    data = int(input())
    arr.append(data)

level = 0
for i in range(N-1, 0, -1):
    if arr[i]>arr[i-1]:continue
    elif arr[i-1]>=arr[i]:
        level += arr[i-1]-arr[i]+1
        arr[i-1] = arr[i]-1

print(level)
