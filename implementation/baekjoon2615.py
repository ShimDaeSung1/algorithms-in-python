import sys
input = sys.stdin.readline

board = []
for i in range(19):
    board.append(list(map(int, input().split())))

# → ↓ ↘ ↗ : 승부가 결정시 연속된 다섯개의 바둑알 중
# 가장 왼쪽에 있는 바둑알의 좌표를 출력해야 하기 때문에
# 방향을 (→ ↓ ↘ ↗)로 설정했다.
dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]

for x in range(19):
    for y in range(19):
        if board[x][y] != 0 :
            color = board[x][y]
            # 4개의 방향
            for i in range(4):
                cnt = 1
                nx = x+dx[i]
                ny = y+dy[i]
                while 0 <= nx <= 18 and 0 <= ny <= 18 and board[nx][ny] == color:
                    cnt += 1
                    if cnt == 5:
                        # 육목 체크
                        if 0<=nx+dx[i]<=18 and 0<=ny+dy[i]<=18 and board[nx+dx[i]][ny+dy[i]] == color:
                            break
                        if 0<=x-dx[i]<=18 and 0<=y-dy[i]<=18 and board[x-dx[i]][y-dy[i]] == color:
                            break
                        print(color)
                        print(x+1, y+1)
                        sys.exit()
                    nx += dx[i]
                    ny += dy[i]
print(0)




















