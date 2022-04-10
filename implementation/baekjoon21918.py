import sys
input = sys.stdin.readline

# 전구의 개수 N과 명령어의 개수 M
# N, M = map(int, input().split())
# light = list(map(int, input().split()))
# for i in range(M):
#     arr = list(map(int, input().split()))
#     if arr[0] == 1 :
#         light[arr[1]-1] = arr[2]
#     elif arr[0] == 2 :
#         for j in range(arr[1]-1, arr[2]):
#             if light[j] == 0:
#                 light[j] = 1
#             else:
#                 light[j] = 0     
#     elif arr[0] == 3:
#         for j in range(arr[1]-1, arr[2]):
#             light[j] = 0
#     elif arr[0] == 4 : 
#         for j in range(arr[1]-1, arr[2]):
#             light[j] = 1
# print(light, end=' ')

n,m=map(int,input().split())
bulbs=list(map(int, input().split()))
for i in range(m):
    a,b,c=map(int, input().split())
    if a==1: bulbs[b-1]=c
    elif a==2 :
        for j in range(b-1,c):
            if bulbs[j]==1:bulbs[j]=0
            else : bulbs[j]=1
    elif a==3:
        for j in range(b-1, c):
            bulbs[j]=0
    elif a==4:
        for j in range(b-1, c):
            bulbs[j]=1
print(*bulbs)
