import sys
input = sys.stdin.readline

# 배열의 크기 N
N = int(input())
B = list(map(int, input().split()))

count = 0
while sum(B)!=0:
    for i in range(N):
        if B[i] % 2 != 0 :
            B[i] = B[i] -1
            count+=1
    if sum(B)!=0:
        for i in range(N):
            B[i] = B[i]//2
        count+=1
    else:
        break
print(count)
