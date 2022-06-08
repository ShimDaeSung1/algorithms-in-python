import sys
input = lambda:sys.stdin.readline().strip()

n = int(input())

t, p = [], []
dp = [0]*(n+1)

for i in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)
M = 0

for i in range(n):
    M = max(M, dp[i])
    if i + t[i] > n :
        continue
    dp[i+t[i]] = max(dp[i+t[i]], M+p[i])
print(max(dp))
