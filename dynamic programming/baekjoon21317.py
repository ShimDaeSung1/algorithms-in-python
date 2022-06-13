n = int(input())
small_energy = [0] # 1칸 점프
big_energy = [0] # 2칸 점프
dp = [0]*(n+1)
dp[0], dp[1] = 0, 0
if n == 1:
    print(0)
    exit()

for i in range(n-1):
    s,b = map(int, input().split())
    small_energy.append(s)
    big_energy.append(b)
k = int(input())

for i in range(2, n+1):
    if i == 2 :
        dp[i] = small_energy[i-1]
    elif i == 3:
        dp[i] = min(dp[i-1]+small_energy[i-1], dp[i-2]+big_energy[i-2])
    else:
        dp[i] = min(dp[i-1]+small_energy[i-1], dp[i-2]+big_energy[i-2])

MIN = 999999
for x in range(1, n-2):
    dpcopy = dp[:]
    # 모든 돌에서 점프하는 경우 따지기
    if dp[x]+k < dp[x+3]:
        dpcopy[x+3] = dpcopy[x]+k
        for t in range(x+4, n+1):
            dpcopy[t] = min(dpcopy[t], dpcopy[t-1]+small_energy[t-1], dpcopy[t-2]+big_energy[t-2])
        if MIN>dpcopy[-1]:
            MIN = dpcopy[-1]
if MIN==999999:
    print(dp[-1])
else:
    print(MIN)


