
import sys
input = sys.stdin.readline

# 식량창고 개수
N = int(input())
# 식량창고의 식량
arr = list(map(int, input().split()))

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
dp = [0]*100

# 다이나믹 프로그래밍(Dynamic Programming) 진행(바텀업)
dp[0] = arr[0]
dp[1] = max(arr[0], arr[1])
for i in range(2, N):
    dp[i] = max(dp[i-1], dp[i-2]+arr[i])
print(dp[N-1])
