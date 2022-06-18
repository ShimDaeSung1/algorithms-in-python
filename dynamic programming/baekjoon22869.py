n, k = map(int, input().split())
Ai = list(map(int, input().split()))

dp = [False]*n
dp[0] = True
for i in range(1, len(Ai)):
    for j in range(i):
        # 쓰는 힘의 양
        if dp[j] == True:
            energy = ((i+1)-(j+1))*(1+abs(Ai[i]-Ai[j]))
            if energy <= k:
                dp[i] = True
                break
if dp[-1] == True:
    print("YES")
else:
    print("NO")


