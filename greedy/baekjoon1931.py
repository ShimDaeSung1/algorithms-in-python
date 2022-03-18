import sys
input = sys.stdin.readline

#회의의 수
N = int(input())
arr = []

for i in range(N):
    a = list(map(int, input().split()))
    arr.append(a)
    
arr.sort(key = lambda x : (x[1], x[0]))

last = 0 # 회의의 마지막 시간을 저장할 변수
conut = 0 # 회의 개수를 저장할 변수

for i, j in arr:
  if i >= last: # 시작시간이 회의의 마지막 시간보다 크거나 같을경우
    conut += 1
    last = j

print(conut)

# sum = 1
# i = 0

# while i < N:
#     if arr[i][0] == arr[i][1]:
#         sum+=1
#         i+=1
#     for j in range(1, N-1):
#         if i >= N-1:
#             i+=1
#             break
#         if i+j > N-1:
#             break
#         if arr[i][1]>arr[i+j][0]:
#              continue
#         else:
#             sum+=1
#             i += j
#             break
    
# print(sum)

    

