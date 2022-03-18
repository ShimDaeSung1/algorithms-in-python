import sys
input = sys.stdin.readline

N = int(input())
h = list(map(int,input().split()))
a = list(map(int,input().split()))

#5
#1 3 2 4 6
#2 7 3 4 1

arr = []
for i in range(N):
    arr.append([h[i],a[i]])

arr.sort(key= lambda x : (x[1], -x[0]))
day = 0
sum = 0
for i in range(N):
    sum += arr[i][0] + arr[i][1]*day
    day+=1
print(sum)