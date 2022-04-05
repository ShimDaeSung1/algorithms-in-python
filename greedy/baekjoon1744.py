# import sys
# input = sys.stdin.readline

# # 수열의 크기 N
# N = int(input())
# arr = []
# for i in range(N):
#     arr.append(int(input()))

# arr.sort(reverse=True)
# i = 0
# sum = 0

# if len(arr) == 1:
#     sum += arr[0]
# if len(arr)%2 == 1:
#     sum+=arr[-1]

# while i < N-1 :
    
#     if arr[i]>1 and arr[i+1]>1:
#         sum += arr[i]*arr[i+1]
#         i+= 2
#     elif arr[i]<0 and arr[i+1]<0:
#         sum += arr[i]*arr[i+1]
#         i+=2
#     elif arr[i] == 0 and arr[i+1]<0:
#         sum += arr[i]*arr[i+1]
#         i+=2
#     else:
#         sum += arr[i]+arr[i+1]
#         i+=2
# print(sum)

from collections import deque


N = int(input())

li = []
for _ in range(N):
    li.append(int(input()))

positive = [num for num in li if num>0]
negative = [num for num in li if num<0]
positive.sort(reverse=True)
negative.sort()
# deque는 양방향 큐, 일반 큐는 선입선출이다.
pos_queue = deque(positive)
neg_queue = deque(negative)

ans = []
while pos_queue:
    if len(pos_queue)>=2:
        a = pos_queue.popleft()
        b = pos_queue.popleft()
        if b == 1:
            ans.append(a)
            ans.append(b)
        else:
            ans.append(a*b)
    else :
        ans.append(pos_queue.popleft())

while neg_queue:
    if len(neg_queue)>=2:
        a = neg_queue.popleft()
        b = neg_queue.popleft()
        ans.append(a*b)
    else:
        break

if 0 in li:
    print(sum(ans))
elif neg_queue:
    print(sum(ans)+neg_queue.popleft())
else:
    print(sum(ans))


