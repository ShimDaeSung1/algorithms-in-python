import sys
input = sys.stdin.readline

#지폐의 금액(10000)
T = int(input())
#가짓수
K = int(input())

coins = []
for _ in range(K):
    # 동전의 금액과 개수
    p,n = map(int, input().split())
    coins.append([p,n])

dp = [0]*(T+1)
dp[0] = 1
for coin, cnt in coins:
    #T원부터 1원까지 내려가며 진행
    for money in range(T,0,-1):
        #현재 동전 개수만큼 for문
        for i in range(1, cnt+1):
            if money-coin*i >= 0: #0원 이상이면
                dp[money] += dp[money-coin*i]
print(dp[T])



