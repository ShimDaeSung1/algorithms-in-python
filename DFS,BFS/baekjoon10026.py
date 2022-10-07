from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
graph = [list(input().strip()) for _ in range(N)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

answer = []

#일반인이 볼때
def bfs_nonRG(RGB, i, j):
    queue = deque([])
    queue.append([i,j])
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            a = x+dx[i]
            b = y+dy[i]
            if 0<=a<N and 0<=b<N :
                if RGB == 'R' and graph[a][b] == 'R' and visited2[a][b] == False:
                    visited2[a][b] = True
                    queue.append([a,b])
                if RGB == 'G' and graph[a][b] == 'G' and visited2[a][b] == False:
                    visited2[a][b] = True
                    queue.append([a,b])
                if RGB == 'B' and graph[a][b] == 'B' and visited2[a][b] == False:
                    visited2[a][b] = True
                    queue.append([a,b])

#적록색약이 볼 때
def bfs_RG(RGB,i,j):
    queue = deque([])
    queue.append([i,j])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            a = x+dx[i]
            b = y+dy[i]
            if 0<=a<N and 0<=b<N:
                if (RGB == 'R' or RGB == 'G') and (graph[a][b] == 'R' or graph[a][b] == 'G') and visited[a][b] == False:
                    visited[a][b] = True
                    queue.append([a,b])
                if RGB == 'B' and graph[a][b] == "B" and visited[a][b] == False:
                    visited[a][b] = True
                    queue.append([a,b])


visited = [[False]*N for _ in range(N)]
visited2 = [[False]*N for _ in range(N)]
cnt = 0
cnt_RG = 0
# 보통사람
for i in range(N):
    for j in range(N):
        if visited2[i][j] == False:
            cnt += 1
            visited2[i][j] = True
            bfs_nonRG(graph[i][j], i, j)
# 적록색약
for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            cnt_RG += 1
            visited[i][j] = True
            bfs_RG(graph[i][j], i, j)

print(cnt, cnt_RG, end=" ")
    
                









