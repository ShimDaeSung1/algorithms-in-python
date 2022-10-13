import sys
input = sys.stdin.readline

# 테스트 케이스 개수
T = int(input())
answer = []
# 최대 10
for i in range(T):
    # 동전의 가지 수 최대 20
    N = int(input())
    # 코인 종류 오름차순
    coin_list = list(map(int, input().split()))
    # 주어진 N가지 동전으로 만들어야 할 금액 최대 1만
    M = int(input())
    # N가지 동전으로 금액 M을 만드는 모든 방법의 수 출력
    dp = [0]*(M+1)
    dp[0] = 1
    for coin in coin_list:
        for i in range(1, M+1):
            if i - coin >= 0 :
                dp[i] += dp[i-coin] 

    answer.append(dp[M])
for i in answer:
    print(i)
