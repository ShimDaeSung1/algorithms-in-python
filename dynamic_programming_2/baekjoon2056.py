import sys
input = sys.stdin.readline

n = int(input())
dp = [0 for _ in range(n+1)]
prev = [[] for _ in range(n+1)]

for i in range(1, n+1):
    time, m, *lst = map(int, input().split())
    dp[i] = time
    for x in lst:
        prev[i].append(x)

for i in range(1, n+1):
    tmp = 0
    for j in prev[i]:
        tmp = max(tmp, dp[j])
    dp[i] += tmp
print(max(dp))



