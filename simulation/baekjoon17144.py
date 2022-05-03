from glob import glob
import sys
input = lambda: sys.stdin.readline().strip()

def mist(x, y, value):
    global r, c, t
    # 인접한 네 방향으로 확산
    amount = value // 5
    for i in range(4):
        if 0 <= x + dx[i] < r and  0 <= y + dy[i] < c :
            if board[x+dx[i]][y+dy[i]] != -1:
                visited[x+dx[i]][y+dy[i]] += amount
                value -= amount
    visited[x][y] += value
    visited[a[0]][0] = -1
    visited[a[1]][0] = -1

    return visited

       
# 행, 열, T초가 지난 후 방에 남은 미세먼지
r,c,t = map(int, input().split())
board = []
for _ in range(r):
    # 공기청정기는 -1이고, 나머지는 미세먼지 양
    board.append(list(map(int, input().split())))

# 방향 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 공기청정기 위치 받기
air = dict()
air['air'] = []
for i in range(len(board)):
    for j in range(len(board[i])):
        # 공기청정기 위치
        if board[i][j] == -1:
            air['air'].append([i])

a = []
for i in air['air']:
    for j in i:
        a.append(j)

# 2. 공기청정기 작동
def clean(arr):
    up = a[0]
    down = a[1]


    # 1열 위쪽 아래로 내리기
    for i in range(up-1, 0, -1):
        arr[i][0] = arr[i-1][0]
    arr[0][0] = 0

    # 1열 아래쪽 위로 올리기
    for i in range(down+2, r):
        arr[i-1][0] = arr[i][0]
    arr[r-1][0] = 0

    #왼쪽으로 이동
    for i in range(0, c-1):
        arr[0][i] = arr[0][i+1]
        arr[r-1][i] = arr[r-1][i+1]
    arr[0][c-1] = 0
    arr[r-1][c-1] = 0

    # r열 위쪽 위로
    for i in range(0, up):
        arr[i][c-1] = arr[i+1][c-1]
    arr[up][c-1] = 0

    # r열 아래쪽 아래로
    for i in range(r-1, down, -1):
        arr[i][c-1] = arr[i-1][c-1]
    arr[down][c-1] =0

    #오른쪽으로 이동
    for i in range(c-1, 1, -1):
        arr[up][i] = arr[up][i-1]
        arr[down][i] = arr[down][i-1]

    arr[up][1] = 0
    arr[down][1] = 0

time = 0
while time < t:
    visited = [[0]*c for _ in range(r)]
    # 1. 미세먼지 확산
    for i in range(len(board)):
        for j in range(len(board[i])):
            # 먼지는 있는데 확산하지 않았다면 확산시켜준다.
            if board[i][j]>0 :
                mist(i, j, board[i][j])
    board = visited
    clean(board)
    time += 1
answer = 2
for i in range(len(board)):
    for j in range(len(board[i])):
        answer += board[i][j]
print(answer)
