import sys
input = sys.stdin.readline

N = int(input())
# 상담
work = [[0,0]]
for _ in range(N):
    l, j = map(int, input().split())
    work.append([l,j])
dp = [0]*(16)

#2일부터 N일까지
for i in range(2, N+2):
    #1일부터 현재의 전날까지
    for j in range(1, i):
        try:
            if i >= j+work[j][0] :
                dp[i] = max(dp[i], dp[j]+work[j][1])
        except:
            continue
print(dp[N+1])




