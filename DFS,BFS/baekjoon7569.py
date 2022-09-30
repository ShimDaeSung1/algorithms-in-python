from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dh = [0, 0, 0, 0, -1, 1]

def bfs(day):
    while queue:
        day += 1
        for _ in range(len(queue)):
            z, x, y = queue.popleft()
            for i in range(6):
                a = z+dh[i]
                b = x+dx[i]
                c = y+dy[i]
                if 0<=a<H and 0<=b<N and 0<=c<M and graph[a][b][c] == 0:
                    graph[a][b][c] = 1
                    queue.append([a,b,c])


    # 토마토 다 익었는지 확인
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            for k in range(len(graph[i][j])):
                if graph[i][j][k] == 0:
                    return -1
    return day-1
    



M,N,H = map(int, input().split())

graph = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
queue = deque([])
for i in range(len(graph)):
    for j in range(len(graph[i])):
        for k in range(len(graph[i][j])):
            if graph[i][j][k] == 1 :
                queue.append([i,j,k])

print(bfs(0))

