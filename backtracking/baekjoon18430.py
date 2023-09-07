import sys
input = sys.stdin.readline

answer = float("-inf")

def backtracking(i,j,sum):
    # for 문 돌리면 시간 초과
    global answer
    if j == m : 
        j = 0
        i += 1
    if i == n :
        return
    
    for k in range(4):
        # 부메랑 생성
        x,y,xx,yy = i+d[k][0], j+d[k][1], i+d[k][2], j+d[k][3]
        # 가능한지 확인
        if x<0 or x>=n or y<0 or y>=m or xx<0 or xx>=n or yy<0 or yy>=m:
            continue
        if visited[x][y] or visited[xx][yy] or visited[i][j]:
            continue
        visited[x][y] = visited[xx][yy] = visited[i][j] = True
        sum += (board[i][j]*2 + board[x][y] + board[xx][yy])
        answer = max(answer, sum)
        backtracking(i, j+1, sum)   
        visited[x][y] = visited[xx][yy] = visited[i][j] = False
        sum -= (board[i][j]*2 + board[x][y] + board[xx][yy])
    backtracking(i, j+1, sum)   

# ㄱ자로 만들어야함. 중앙부터
# 중심이 되는 칸은 강도가 두배
# 부메랑은 한 개만 만들어도 됨.
d = {0:[0,-1,1,0], 1:[0,-1,-1,0], 2:[-1,0,0,1], 3:[1,0,0,1]}

n,m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

backtracking(0,0,0)
if answer == float("-inf"): answer = 0
print(answer)
