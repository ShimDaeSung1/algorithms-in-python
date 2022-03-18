import sys
input = sys.stdin.readline

#음의 개수N, 첫 항A, 공차 D
N, A, D = map(int, input().split())

#참가자들의 음을 나타냄
arr = list(map(int, input().split()))

cnt = 0
x = 0
for i in range(N):
    if arr[i] == A + (x*D):
        cnt += 1
        x += 1
print(cnt)
