import sys
input = sys.stdin.readline

N, M = map(int, input().split())
#S에 포함되어있는 문자열
S = []
check_list = []
for _ in range(N):
    S.append(input().rstrip())

for _ in range(M):
    check_list.append(input().rstrip())

cnt = 0
for i in check_list:
    if i in S:
        cnt += 1

print(cnt)