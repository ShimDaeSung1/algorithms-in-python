import sys
input = lambda: sys.stdin.readline().strip()

N, M = map(int, input().split())
board = [list(map(int, input().split()))for _ in range(N)]
moves = [tuple(map(int, input().split())) for _ in range(M)]

# ←, ↖, ↑, ↗, →, ↘, ↓, ↙ (1번부터 시작이므로 앞에 0,0 추가)
dx8 = ("empty", 0, -1, -1, -1, 0, 1, 1, 1)
dy8 = ("empty", -1, -1, 0, 1, 1, 1, 0, -1)

# 대각선 방향
dx4 = (-1, 1, -1, 1)
dy4 = (-1, -1, 1, 1)

clouds = [(N-1, 0),(N-1, 1),(N-2,0),(N-2,1)] #구름 좌표

for d, s in moves:
    # 모든 구름 이동
    move_clouds = []
    for x, y in clouds:
        # 구름들을 d방향으로 s만큼 이동(구름의 좌표는 연결되어 있으므로 %N을 해준다. 모듈러 연산)
        nx = (x+dx8[d]*s)%N
        ny = (y+dy8[d]*s)%N
        board[nx][ny] += 1
        move_clouds.append((nx, ny))
    for x, y in move_clouds:
        # 이동한 구름들의 대각 4방향 조사 후 count만큼 물의 양 추가
        count = 0
        for i in range(4):
            if 0<=x+dx4[i]<N and 0<=y+dy4[i]<N and board[x+dx4[i]][y+dy4[i]] > 0:
                count+=1
        board[x][y] += count
    clouds = []
    for x in range(N):
        for y in range(N):
            if board[x][y] >= 2 and (x,y) not in move_clouds:
                board[x][y] -= 2
                clouds.append((x,y))

result = 0
for x in range(N):
    for y in range(N):
        result += board[x][y]
print(result)



    

