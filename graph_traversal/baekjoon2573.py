import sys
input = sys.stdin.readline
from collections import deque

# 1. 빙산의 상하좌우가 0(바다)이면 바다 개수만큼 -1
# 2. 빙산이 두개 이상으로 나누어지면 정답 출력
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n,m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

answer = 0
ice = []
for i in range(n):
    for j in range(m):
        if graph[i][j] > 0 : ice.append([i,j])

while True:
    br = 0
    needMinus = []
    visited = [[False for _ in range(m)] for _ in range(n)]
    for i, j in ice:
        # 빙산이있고 방문하지 않은경우 
        if graph[i][j] > 0 and visited[i][j] == False:
            # 빙산 조각 하나 추가
            br += 1
            if br >= 2:
                print(answer)
                exit()
            visited[i][j] = True
            queue = deque([])
            queue.append([i,j])
            while queue:
                x,y = queue.popleft()
                cnt = 0
                for k in range(4):
                    nx = x+dx[k]
                    ny = y+dy[k]
                    # 빙산 추가
                    if 0<=nx<n and 0<=ny<m :
                        if visited[nx][ny] == False and graph[nx][ny] > 0:
                            visited[nx][ny] = True
                            queue.append([nx,ny])
                        # 바다일경우
                        elif graph[nx][ny] == 0:
                            cnt += 1
                if cnt > 0 :
                    needMinus.append([x,y,cnt])
    for x,y,count in needMinus:
        graph[x][y] = max(0, graph[x][y]-count)
    if br >= 2:
        break
    if br == 0:
        answer = 0
        break
    answer += 1
print(answer)
