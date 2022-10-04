from collections import deque
from copy import deepcopy
import sys
input = sys.stdin.readline

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(visited, i,j,k):
    queue = deque([])
    queue.append([i,j])
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            a = x+dx[i]
            b = y+dy[i]
            if 0<=a<N and 0<=b<N and board[a][b] > k and visited[a][b] == False:
                queue.append([a,b])
                visited[a][b] = True
    return visited

max_area = 0
for k in range(max(map(max, board))):
    visited = [[False]*N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            # 높이보다 높으므로 안 잠기는 부분
            if board[i][j] > k and visited[i][j] == False:
                visited[i][j] = True
                cnt += 1
                visited = bfs(visited, i, j, k)
    max_area = max(cnt, max_area)

print(max_area)
                
    

