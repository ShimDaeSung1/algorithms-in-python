from collections import deque
from copy import deepcopy
import sys
input = sys.stdin.readline
dx = [0,0,-1,1]
dy = [1,-1,0,0]
#가로, 세로
n,m = map(int, input().split())

graph = [list(map(int, input().strip())) for _ in range(n)]

# 3차원 행렬을 통해 벽의 파괴를 파악한다. visited[x][y][0]은 벽 파괴 가능, [x][y][1]은 불가능을 나타냄
visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

def bfs(x,y,z):
    queue = deque()
    queue.append((x,y,z))

    while queue:
        a,b,c = queue.popleft()
        if a == n-1 and b == m-1 :
            return visited[a][b][c]
        for i in range(4):
            nx = a+dx[i]
            ny = b+dy[i]
            if 0<=nx<n and 0<=ny<m :
                # 다음 이동할 곳이 벽이고, 벽파괴 기회를 사용하지 않은 경우
                if graph[nx][ny] == 1 and c == 0:
                    visited[nx][ny][1] = visited[a][b][0] + 1
                    queue.append((nx,ny,1))
                # 벽이 없을 경우, 방문하지 않았다면 벽파괴 기회를 사용했는지 체크 후 똑같은 곳에 +1 
                if graph[nx][ny] == 0 and visited[nx][ny][c] == 0:
                    visited[nx][ny][c] = visited[a][b][c] + 1
                    queue.append((nx,ny,c))
    if visited[n-1][m-1][0] == 0 and visited[n-1][m-1][1] == 0:
        print("-1")
        exit()
bfs(0,0,0)
print(max(visited[n-1][m-1]))


