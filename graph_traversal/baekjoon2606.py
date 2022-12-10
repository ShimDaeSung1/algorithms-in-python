import sys
input = sys.stdin.readline
from collections import deque

# 컴퓨터의 수
n = int(input())

# 연결되어있는 컴퓨터의 쌍의 수
m = int(input())

visited = [False]*(n+1)
network = [[0 for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    start, end = map(int, input().split())
    network[start][end] = 1
    network[end][start] = 1

# 1번이 바이러스에 걸렸을 때
def bfs(start):
    q = deque([])
    q.append(start)
    visited[start] = 1
    count = 0
    while q:
        start = q.popleft()
        for i in range(1, len(network[start])):
            if network[start][i] == 1 and visited[i] == False:
                q.append(i)
                visited[i] = True
                count += 1
    return count

print(bfs(1))

