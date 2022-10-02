from collections import deque
import sys
input = sys.stdin.readline

dx = [0,0,1,-1]
dy = [1,-1,0,0]

n = int(input())
graph = [list(input().strip()) for _ in range(n)]

for i in range(len(graph)):
    int_list = list(map(int, graph[i]))
    graph[i] = int_list

answer = []
def bfs(cnt):
    l = len(graph)
    queue = deque([])
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1 :
                graph[i][j] = 0
                queue.append([i,j])
                cnt += 1
                house = 1
                while queue:
                    x,y = queue.popleft()
                    for k in range(4):
                        a = x+dx[k]
                        b = y+dy[k]
                        if 0<=a<n and 0<=b<n and graph[a][b] == 1:
                            graph[a][b] = 0
                            house += 1
                            queue.append([a,b])
                answer.append(house)
    return cnt

cnt_house = bfs(0)
print(cnt_house)
answer.sort()
for i in answer:
    print(i)






