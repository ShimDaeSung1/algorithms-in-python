from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

visited = [[False]*(m) for _ in range(n)] 

#최단 경로는 bfs
def bfs(x, y):
    queue = deque()
    queue.append((x,y))

    while queue : 
        x, y = queue.popleft()

        for i in range(4):
            a = x+dx[i]
            b = y+dy[i]
            if 0 <= a < n and 0 <= b < m and graph[a][b] == 1:
                if visited[a][b] :
                    continue
                else:
                    graph[a][b] = graph[x][y]+1
                queue.append((a,b))
bfs(0,0)
print(graph[n-1][m-1])
            
