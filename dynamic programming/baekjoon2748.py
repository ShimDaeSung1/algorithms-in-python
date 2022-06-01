# import sys
# input = lambda: sys.stdin.readline().strip()
# sys.setrecursionlimit(10**6)

# def fibonacci(n):
#     if n <= 1:
#         return n
#     return fibonacci(n-1) + fibonacci(n-2)
# n = int(input())
# print(fibonacci(n))

n = int(input())
arr = [0]*(n+1)
arr[1] = 1
for i in range(2, n+1):
    arr[i] = arr[i-1] + arr[i-2]
print(arr[n]) 
