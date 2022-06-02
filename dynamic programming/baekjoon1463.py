n = int(input())
dp = [0]*(n+1)

for i in range(2, n+1):
    # 1을 빼는 방법
    dp[i] = dp[i-1]+1
    # 3으로 나누는 방법도 시도
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)
    # 2로 나누는 방법도 시도
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
print(dp[n])
