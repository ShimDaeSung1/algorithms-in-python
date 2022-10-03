from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 테스트케이스 개수 T
T = int(input())

def bfs(graph, cnt):
    queue = deque([])
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == 1:
                cnt += 1
                queue.append([i,j])
                graph[i][j] = 0
                while queue:
                    x, y = queue.popleft()
                    for k in range(4):
                        a = x+dx[k]
                        b = y+dy[k]
                        if 0<=a<M and 0<=b<N and graph[a][b] == 1:
                            graph[a][b] = 0
                            queue.append([a,b])
    return cnt-1

answer = []
for _ in range(T):
    # 가로M, 세로N, 배추 개수 K
    M, N, K = map(int, input().split())
    graph = [[0]*N for _ in range(M)]
    for _ in range(K):
        x, y = map(int, input().split())
        graph[x][y] = 1
    answer.append(bfs(graph, 0))
for i in answer:
    print(i)
    




