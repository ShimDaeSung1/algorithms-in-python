from filecmp import cmp
from ntpath import join
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = []
for i in range(N):
    data = input().strip()
    arr.append(data)

str = ''.join(arr) #다 이어붙인 문자열 
len_str = len(str) #그 문자열의 길이
need_ = M-len_str # 필요한 _의 개수
arr_origin = arr

arr = sorted(arr[0:N-1], key=lambda x : (x[0:]))
arr.append(arr_origin[N-1])

while need_ > 0 :
    for i in range(0, N-1):
        arr[i] += "_"
        need_ -= 1
        if need_ == 0:
            break

for i in range(N):
    for j in range(N):
        if arr[j].startswith(arr_origin[i]):
            index = j
            arr_origin[i] = arr[j]
        else:
            continue    
        


str = ''.join(arr_origin)
print(str)


# n, m=map(int, input().split())
# l=[]
# for _ in range(n):
#     s=input()
#     l.append(s)
#     m-=len(s)
# count=m//(n-1)
# mcn=m-count*(n-1)
# ecn=n-1-mcn
# for i in range(1, n):
#     if ecn==0:
#         for _ in range(count+1):
#             l[i]='_'+l[i]
#         mcn-=1
#         continue
#     if mcn==0 or ord(l[i][0])<93:
#         for _ in range(count):
#             l[i]='_'+l[i]
#         ecn-=1
#         continue
#     if ord(l[i][0])>95:
#         for _ in range(count+1):
#             l[i]='_'+l[i]
#         mcn-=1
#         continue
# print(*l, sep="")

