import sys
input  = sys.stdin.readline
# Pypy3
n, m, r = map(int, input().split())

data = [list(map(int, input().split()))for _ in range(n)]

for _ in range(r):
    for i in range(min(n, m)//2):
        # x,y는 돌려지는 배열 중 가장 첫번째 배열 인덱스
        x, y = i, i
        temp = data[x][y]

        #좌측 : 아래로
        for j in range(i+1, n-i):
            x = j
            prev_value = data[x][y]
            data[x][y] = temp
            temp = prev_value
        #아래측 : 오른쪽으로
        for j in range(i+1, m-i):
            y = j
            prev_value = data[x][y]
            data[x][y] = temp
            temp = prev_value
        # 우측 : 위로
        for j in range(i+1,n-i):
            x = n-1-j
            prev_value = data[x][y]
            data[x][y] = temp
            temp = prev_value
        # 위 : 왼쪽으로
        for j in range(i+1, m-i):
            y = m-1-j
            prev_value = data[x][y]
            data[x][y] = temp
            temp = prev_value
for i in range(n):
    for j in range(m):
        print(data[i][j],end=' ')
    print()
