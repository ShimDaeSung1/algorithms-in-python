from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, cnt):
    queue = deque([])
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == 0:
                queue.append([i,j])
                cnt += 1
                ans = 1
                graph[i][j] = 1
                while queue:
                    x, y = queue.popleft()
                    for k in range(4):
                        a = x+dx[k]
                        b = y+dy[k]
                        if 0<=a<M and 0<=b<N and graph[a][b] == 0:
                            ans += 1
                            graph[a][b] = 1
                            queue.append([a,b])
                answer.append(ans)
    return cnt


M, N, K = map(int, input().split())
graph = [[0]*N for _ in range(M)]
answer = []
for _ in range(K):
    Lx,Ly,Rx,Ry = map(int, input().split())
    for i in range(Ly, Ry):
        for j in range(Lx, Rx):
            graph[i][j] = 1

cnt = bfs(graph, 0)
print(cnt)
answer.sort()
for i in answer:
    print(i, end=" ")



    
