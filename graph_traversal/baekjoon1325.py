import sys
input = sys.stdin.readline
from collections import deque

#n대의 컴퓨터
n, m = map(int,input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[b].append(a)

def bfs(start):
    global max_cnt
    cnt = 1
    q = deque([])
    visited = [False]*(n+1)
    visited[start] = True
    q.append(start)

    while q:
        x = q.popleft()
        for i in graph[x]:
            if visited[i] == False:
                visited[i] = True
                cnt += 1
                q.append(i)
    return cnt
answer = []
max_cnt = 0
for i in range(1,n+1):
    cnt = bfs(i)
    if cnt > max_cnt:
        max_cnt = cnt
    answer.append([i, cnt])
answer.sort(key = lambda x : (x[1], x[0]))
for i in answer:
    if i[1] == max_cnt:
        print(i[0], end=' ')
        

    