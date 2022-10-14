import sys
input = sys.stdin.readline

# 물품의 수 N(100), 버틸 수 있는 무게 K(10만)
N, K = map(int, input().split())
# 각 물건의 무게(10만)와 가치(1000)가 주어짐
thing = [[0,0]]
for i in range(N):
    thing.append(list(map(int, input().split())))

dp = [[0]*(K+1) for _ in range(N+1)]

#배낭에 넣을 수 있는 물건들의 가치합의 최댓값 구하기
#배낭 문제는 냅색(Knapsack) 알고리즘을 사용한다.
for i in range(1, N+1):
    # 물건 별로 돌면서 무게 추가, 가치 확인 
    for j in range(1, K+1):
        w, v = thing[i]
        if j < w :
            dp[i][j] = dp[i-1][j] 
        else : 
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)
print(max(max(dp)))








