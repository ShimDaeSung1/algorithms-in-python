from collections import deque
from copy import deepcopy
import sys
input = sys.stdin.readline

def bfs():
    copy_graph = deepcopy(graph)
    queue = deque([])
    for i in range(n):
        for j in range(m):
            if copy_graph[i][j] == 2:
                queue.append([i,j])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            a = x+dx[i]
            b = y+dy[i]
            if 0<=a<n and 0<=b<m and copy_graph[a][b] == 0:
                copy_graph[a][b] = 2
                queue.append([a,b])
    global answer
    cnt = 0
    for i in range(n):
        cnt += copy_graph[i].count(0)
    answer = max(answer, cnt)


def makeWall(cnt):
    if cnt == 3:
        bfs()
        return
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                makeWall(cnt+1)
                graph[i][j] = 0

n, m = map(int, input().split())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

graph = [list(map(int, input().split())) for _ in range(n)]
answer = 0
makeWall(0)
print(answer)
