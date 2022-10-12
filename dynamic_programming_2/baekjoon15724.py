import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph_people = [list(map(int, input().split())) for _ in range(n)]

k = int(input())
want_cnt = []
for i in range(k):
    a,b,c,d = map(int, input().split())
    want_cnt.append([[a,b],[c,d]])
dp = [[0]*(m+1) for _ in range(n+1)]
# dp채우기
for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j] = graph_people[i-1][j-1] + dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1]


answer = []
for i in want_cnt:
    x1, y1 = i[0]
    x2, y2 = i[1]
    # print(x1,x2,y1,y2)
    cnt = dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1]
    answer.append(cnt)
    
for i in answer:
    print(i)