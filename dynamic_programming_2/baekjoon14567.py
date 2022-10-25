
import sys
input = sys.stdin.readline

# 과목의 수, 선수 조건의 수
N, M = map(int, input().split())

subject = []
for _ in range(M):
    # a번 과목이 b번 과목의 선수과목
    a, b = map(int, input().split())
    subject.append([a,b])
# 1번 과목부터 N번 과목까지 차례대로 최소 몇 학기에 이수 가능한지를 한 줄에 공백으로 구분하여 출력
subject.sort(key = lambda x : (x[0],x[1]))
dp = [1]*(N+1)

for i in range(len(subject)):
    a, b = subject[i]
    dp[b] = max(dp[b], 1+dp[a])
for i in range(1, len(dp)):
    print(dp[i], end=" ")

