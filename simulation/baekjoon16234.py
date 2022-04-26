import sys
input = sys.stdin.readline
from collections import deque

graph = []
n,l,r = map(int,input().split())
for _ in range(n):
    graph.append(list(map(int,input().split())))

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(a,b):
    q = deque()
    temp = []
    q.append((a,b))
    temp.append((a,b))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # bfs를 호출한 지역에서 이동 가능한 부분 체크, 방문 안 한곳만
            if 0<=nx<n and 0<=ny<n and visited[nx][ny] == 0:
                # 국경선을 공유하는 두 나라의 인구 차이가 L이상, R이하일 경우 두 나라가 공유하는 국경선을 하루동안 연다.
                if l <= abs(graph[nx][ny]-graph[x][y]) <= r:
                    visited[nx][ny] =1
                    q.append((nx,ny))
                    temp.append((nx,ny))
    return temp





result = 0
while 1:
    # 인덱스를 1부터 사용하기 위함
    visited = [[0]*(n+1) for _ in range(n+1)]
    flag = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                visited[i][j] = 1
                country = bfs(i,j)
                # bfs(i,j)를 통해, 넓이 우선 탐색으로 모든 곳을 돌아서 temp를 받는다.
                #위의 조건에 의해 열어야 하는 국경선이 모두 열렸다면, 인구 이동을 시작한다.
                if len(country) > 1: #bfs를 통해 한 턴(다 돌고 인구 이동을 시작하게 되는 턴)에 받은 좌표가 두개 이상일 경우, 즉 연합이 한 개의 나라 이상일 경우
                    # 국경선이 열려있다면 flag를 1로 바꿔서 인구 이동 시작
                    flag = 1
                    #연합을 이루고 있는 각 칸의 인구수는 (연합의 인구수)/(연합을 이루고 있는 칸의 개수)가 된다. 편의상 소수점은 버린다.
                    number = sum([graph[x][y] for x, y in country]) // len(country)
                    for x, y in country:
                        graph[x][y] = number
                
    if flag == 0:
        break
    result += 1
print(result)
    
