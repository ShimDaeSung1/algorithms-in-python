import sys
input = sys.stdin.readline
from collections import deque # deque를 통해 시간복잡도를 줄였다.


# bfs 탐색
def bfs(day):

    # 큐에 탐색해야 하는 노드 없을 때까지 실행
    while queue:

        day += 1  # 일수 증가

        # 큐에 있는 노드 수만큼 탐색
        for _ in range(len(queue)):

            a, b = queue.popleft()  # 큐에 있는(탐색해야 하는) 노드의 좌표
            # 4방향 확인
            for i in range(4):
                x = a + dx[i]
                y = b + dy[i]

                # 아직 방문하지 않은 미로중에 토마토가 있는 경우
                if -1 < x < n and -1 < y < m and graph[x][y] == 0:

                    # 방문처리
                    graph[x][y] = 1

                    # 탐색할 곳을 추가
                    queue.append([x, y])

    # 익지 않은 토마토 남아있는 경우 -1 반환
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == 0:
                return -1

    # 모두 익은 경우 일수 출력
    return day - 1


m, n = map(int, input().split())

# 2차원 미로
graph = [list(map(int, input().split())) for _ in range(n)]

# 좌/우/위/아래 방향 이동
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 익은 토마토 확인
queue = deque([])
for i in range(len(graph)):
    for j in range(len(graph[i])):
        if graph[i][j] == 1:
            queue.append([i, j])

print(bfs(0))