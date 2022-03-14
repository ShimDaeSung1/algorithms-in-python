import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
len = sum(arr)
arr.sort()
cost = 0
for i in arr:
  len -= i
  cost += len*i

print(cost)


