import sys
input = sys.stdin.readline

n, m = map(int, input().split())
if n == 0 :
  print(0)
else :
  data = list(map(int, input().split()))

  target = 0
  result = 1
  for i in range(n-1, -1, -1) :
    target += data[i]
    if target > m :
      result += 1
      target = data[i]

  print(result)

# N,M=map(int,input().split())
  
# sum = 0
# box = 1
# if N >= 1:
#   W = list(map(int, input().split()))
#   W.sort()
# elif N == 0 :
#   box = 0

# for i in range(N):
#   sum += W[i]
#   if sum > M:
#     sum = W[i]
#     box +=1
#   elif sum == M :
#     if i == N-1:
#       break
#     else:
#       sum = 0
#       box +=1

# print(box)
    
