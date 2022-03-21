import sys
input = sys.stdin.readline

# ^=는 각 비트의 비교 위치에서 1이 짝수 개수면 0, 홀수이면 1, 둘 다 0이면 0
def xor(a, b):
    for row in range(a + 1):
        for col in range(b + 1):
            matrix[row][col] ^= 1

# 세로크기 N, 가로크기 M
n, m = map(int, input().split())
matrix = [list(map(int, input().rstrip())) for __ in range(n)]
cnt = 0


# for row in range(N-1, -1, -1):
for row in range(n - 1, -1, -1):
    for col in range(m - 1, -1, -1):
        if matrix[row][col]:
            cnt += 1
            xor(row, col)
print(cnt)
