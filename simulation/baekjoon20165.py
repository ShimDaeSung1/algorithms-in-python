import sys
input = lambda: sys.stdin.readline().strip()
sys.setrecursionlimit(10**6)

def slick(x, y, d):
    global total
    temp = state[x][y]
    if state[x][y] == 'S':
        state[x][y] = 'F'
        total += 1
    if temp == 'S':   
        for i in range(1, board[x][y]):
            if 0<=x+(i*key[d][0])<r and 0<=y+(i*key[d][1])<c:
                slick(x+(i*key[d][0]), y+(i*key[d][1]), d)
    else:
        return

#행 개수, 열 개수, 라운드 개수
r, c, R = map(int, input().split())
board = [list(map(int, input().split()))for _ in range(r)]
# S는 서있는 상태, F는 넘어진 상태다.
state = [['S']*c for _ in range(r)]
key = {'E':(0,1), 'W':(0,-1), 'S':(1,0), 'N':(-1,0)}
total = 0
for _ in range(R):
    # x행 y열의 도미노를 D방향으로 민다.
    x, y, d = list(input().split()) 
    x = int(x)-1
    y = int(y)-1
    # 수비수는 a행 b열의 도미노를 다시 세운다.
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    # 도미노 밀기
    if state[x][y] == "S":
        slick(x,y,d)
    # 다시 세우기
    state[a][b] = 'S'

print(total)
for i in range(len(board)):
    for j in range(len(board[i])):
        print(state[i][j], end=' ')
    print()






