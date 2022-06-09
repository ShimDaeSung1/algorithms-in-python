n = int(input())
glass = [0]
for i in range(n):
    glass.append(int(input()))
dp = [0]
dp.append(glass[1])
if n > 1 :
    dp.append(glass[1]+glass[2])

for i in range(3, n+1):
    dp.append(max(dp[i-1], dp[i-3]+glass[i]+glass[i-1], dp[i-2]+glass[i]))
print(max(dp))
