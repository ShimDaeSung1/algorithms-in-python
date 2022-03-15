import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))

arr.sort()
arr_2 = []

lose = 0
if len(arr)%2 == 1:
    for i in range(1, N-1):
        arr_2.append(arr[i-1]+arr[N-i-1])
    arr_2.append(arr[N-1])
    lose = max(arr_2)
else:
    for i in range(1, N):
        arr_2.append(arr[i-1]+arr[N-i])
    lose = max(arr_2)

print(lose)

