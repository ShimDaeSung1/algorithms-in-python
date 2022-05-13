from collections import deque
import sys
input = lambda:sys.stdin.readline().strip()

n,m,energy = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
s_x, s_y = list(map(int, input().split()))
people = [list(map(int, input().split())) for _ in range(m)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(s_x, s_y):
    visited = [[-1]*n for _ in range(n)]
    queue = deque()
    queue.append((s_x,s_y))
    visited[s_x][s_y] = 0

    while queue:
        pop_x, pop_y = queue.popleft()

        for i in range(4):
            n_x, n_y = pop_x+dx[i], pop_y+dy[i]

            if n_x < 0 or n_x >= n or n_y <0 or n_y >= n :
                continue
            if graph[n_x][n_y] == 1 or visited[n_x][n_y] != -1:
                continue

            visited[n_x][n_y] = visited[pop_x][pop_y] + 1
            queue.append((n_x,n_y))
    return visited

def check_dist(visited, people):
    i = 0
    for p_x, p_y, a_x, a_y in people:
        people[i].append(visited[p_x-1][p_y-1])
        i+=1
    # 내림차순 정리하여 가장 오른쪽부터 가까운 거리, 행이 작은, 열이 작은 순
    people.sort(key=lambda x : (-x[4], -x[0],-x[1]))

def solve(s_x, s_y):
    global energy
    while people:
        visited = bfs(s_x-1, s_y-1)
        check_dist(visited, people)
        p_x, p_y, a_x, a_y, dist = people.pop()

        for temp in people:
            # 다시 BFS를 돌려야하므로 각 승객들의 거리를 초기화(0)
            temp.pop()
        # 다시 bfs불러서 뽑은 가장 가까운 승객부터 목적지 까지의 거리 출력
        visited = bfs(p_x-1, p_y-1)
        dist2 = visited[a_x-1][a_y-1]
        # 목적지의 위치를 다시 시작 위치로
        s_x, s_y = a_x, a_y

        # 사람이나(dist) 목적지(dist2) 까지 도달할 수 없다면 -1출력
        # 즉 모든 승객을 빠짐없이 성공적으로 데려다 줄 수 없는지 여부 확인
        if dist == -1 or dist2 == -1 :
            print(-1)
            return
        # 승객을 태우러 갔을 때 연료 소모가 더 크면(태우러 갈 수 없다면) 취소
        energy -= dist
        if energy < 0 :
            break
        # 승객을 태우러 갈 순 있는데,
        # 승객을 내려주러 갔을 때 연료 소모가 더 크면 취소
        energy -= dist2
        if energy < 0 :
            break
        # 성공
        energy += dist2*2
    if energy < 0:
        print(-1)
    else:
        print(energy)

solve(s_x, s_y)




