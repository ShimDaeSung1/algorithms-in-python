import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [list(map(int,list(input()))) for _ in range(N)]
B = [list(map(int,list(input()))) for _ in range(N)]

def change(x, y):
    for i in range(x, x+3):
        for j in range(y, y+3):
            A[i][j] = 1-A[i][j]

def check_equal():
    for i in range(N):
        for j in range(M):
            if A[i][j] != B[i][j] :
                return 0
    return 1

cnt = 0
for i in range(N-2):
    for j in range(M-2):
        if A[i][j] != B[i][j]:
            change(i,j)
            cnt += 1

if check_equal():
    print(cnt)
else:
    print(-1)