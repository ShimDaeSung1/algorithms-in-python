# import sys
# input = sys.stdin.readline

# n = int(input())
# Hi = list(map(int,input().split()))
# Ai = list(map(int,input().split()))
# sum = 0

# for i in range(n):
#     if i == 0 :
#         sum += max(Hi)
#         index = Hi.index(max(Hi))
#         Hi[index] = 0
#         for j in range(n):
#             Hi[j]+=Ai[j]  
#     else:
#         sum+=max(Hi)
#         index = Hi.index(max(Hi))
#         Hi[index]=0
#         for j in range(n):
#             Hi[j]+=Ai[j]    
        
# print(sum)

import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
total = []
ans = 0
day = 0
arr = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
for i in range(n):
    total.append([arr[i],arr2[i]])

total.sort(key = lambda x : (x[1], -x[0]))

for i in range(len(total)):
    for j in range(len(total[i])):
         print(total[i][j], end=' ')
    print()


# for i in range(n):
#     ans += total[i][0] + total[i][1] * day
#     day += 1
# print(ans)