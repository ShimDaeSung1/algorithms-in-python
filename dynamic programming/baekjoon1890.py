n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
answer = 0

dp = [[0]* n  for _ in range(n)] # i,j 까지 올 수 있는 경우의 수를 저장
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if i == n-1 and j == n-1 : #끝에 도달
            print(dp[i][j])
            break
        cur_cnt = board[i][j]
        # 오른쪽으로 가기
        if j+cur_cnt < n:
            dp[i][j+cur_cnt] += dp[i][j]
        if i+cur_cnt < n:
            dp[i+cur_cnt][j] += dp[i][j]



