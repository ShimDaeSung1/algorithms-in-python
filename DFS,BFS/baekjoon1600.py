from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    visited = [[[0 for _ in range(K+1)] for _ in range(W)] for _ in range(H)]
    queue = deque([])
    queue.append([0,0,K])
    while queue:
        x,y,z = queue.popleft()
        if x == H-1 and y == W-1 :
            return visited[x][y][z]
        for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if 0<=nx<H and 0<=ny<W and visited[nx][ny][z] == 0 and graph[nx][ny] == 0:
                    visited[nx][ny][z] = visited[x][y][z] + 1 
                    queue.append([nx,ny,z])
        if z>0:
            for i in range(8):
                nx = x+ches_x[i]
                ny = y+ches_y[i]
                if 0<=nx<H and 0<=ny<W and visited[nx][ny][z-1] == 0 and graph[nx][ny] == 0:
                    visited[nx][ny][z-1] = visited[x][y][z] + 1
                    queue.append([nx,ny,z-1])            
    return -1


#K번만 움직일 수 있다.
K = int(input())
#가로길이W, 세로길이H
W, H = map(int, input().split())

ches_x = [-2, -1, 1, 2, 2, 1, -1, -2]
ches_y = [1, 2, 2, 1, -1, -2, -2, -1]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

graph = [list(map(int, input().split())) for _ in range(H)]
print(bfs())
