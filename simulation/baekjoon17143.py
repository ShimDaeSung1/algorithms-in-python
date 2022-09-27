
r,c,m = map(int, input().split())
board = [[[]]*c for _ in range(r)]

for _ in range(m):
    x,y,s,d,z = map(int, input().split())
    x -= 1
    y -= 1
    d -= 1
    board[x][y] = [s,d,z]


def move():
    new_board = [[[]]*c for _ in range(r)]
    global board
    for x in range(r):
        for y in range(c):
            nx, ny = x, y
            if board[x][y] : 
                s,d,z = board[x][y][0:3]
                for i in range(s):
                    nx += dx[d]
                    ny += dy[d]
                    if not (0<=nx<r and 0<=ny<c):
                        nx -= 2*dx[d]
                        ny -= 2*dy[d]
                        if d in [0,2]:
                            d += 1
                        elif d in [1,3]:
                            d -= 1            

                if new_board[nx][ny]: 
                    if z > new_board[nx][ny][2]:
                        new_board[nx][ny] = [s,d,z]
                else :
                    new_board[nx][ny] = [s,d,z]
        
    return new_board


#상하우좌
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
answer = 0
fishing = [0,0]

for i in range(c):
    if i != 0 :
        fishing[1] += 1
    x, y = fishing
    dir = 1
    for j in range(2*r):
        if board[x][y] and board[x][y][2] > 0:
            answer += board[x][y][2]
            board[x][y] = []
            # for k in range(len(shark)):
            #     if x == shark[k][0] and y == shark[k][1]:
            #         shark.pop(k)
            #         break
            break
        else : 
            x += dx[dir]
            if x == r-1:
                dir = 0
    # 상어 이동
    board = move()
print(answer)






