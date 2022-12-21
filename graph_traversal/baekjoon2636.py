import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

def bfs():
    # 모서리 체크하기
    q = deque([(0,0)])
    global graph
    melt = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[0 for _ in range(m)] for _ in range(n)]
    nx = [0,0,-1,1]
    ny = [-1,1,0,0]
    
    while q:
        x,y = q.popleft()
        #공기에서만 탐색해야함
        if graph[x][y] == 0:
            for i in range(4):
                dx = x+nx[i]
                dy = y+ny[i]
                #범위 안이라면
                if 0<=dx<n and 0<=dy<m and visited[dx][dy] == 0:
                    if melt[dx][dy] == 0 and graph[dx][dy] == 1:
                        melt[dx][dy] = 1
                    if melt[dx][dy] == 0 and graph[dx][dy] == 0:
                        q.append([dx,dy])
                        visited[dx][dy] = 1
    return melt
cnt = 0
cnt_2 = 0
while True:
    answer = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                answer += 1
    if answer == 0 :
        break

    cnt_2 = answer
    melt = bfs()
    cnt += 1
    for i in range(n):
        for j in range(m):
            if melt[i][j] == 1:
                graph[i][j] = 0
print(cnt)
print(cnt_2)
