import sys
input = lambda: sys.stdin.readline().strip()

# n세대 커브는 n-1세대 커브 끝점 + n-1세대*90도
# 세대별 선의 개수
# 0세대 : 2^0
# 1세대 : 2^1
# 2세대 : 2^2 , 즉 n세대 : 2^n
# 방향에 의하면 다음과 같다.

n = int(input())

# x, y는 0이상 100이하 므로 100도 포함
graph = [[0] * 101 for _ in range(101)]
#방향 d :  → ↑ ← ↓
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]
# 0세대 : [0]
# 1세대 : [0,1]
# 2세대 : [0,1,2,1]
# 커브 리스트를 만들고 방향을 더해가면 끝     

for i in range(n):
    # x,y는 드래곤커브의 시작 점, d는 시작 방향, g는 세대
    x, y, d, g = map(int, input().split(' '))
    graph[x][y] = 1

    # 커브 리스트 만들기
    curve = [d] #시작 방향
    for j in range(g): # 세대 수
        for k in range(len(curve) - 1, -1, -1):
            # 드래곤 커브 선을 거꾸로 확인하면서 늦게 만들어진 것부터 90도 뒤집는다. 즉 
            # 90도 뒤집으면 → ↑ ← ↓ 순이다.
            # 마지막으로 만들어진 것부터 거꾸로 탐색하면서 방향만 +1 해주면 90도 뒤집힘
            curve.append((curve[k] + 1) % 4)

    # 드래곤 커브 만들기
    for j in range(len(curve)):
        x += dx[curve[j]]
        y += dy[curve[j]]
        if x < 0 or x >= 101 or y < 0 or y >= 101:
            continue

        graph[x][y] = 1

answer = 0
for i in range(100):
    for j in range(100):
        if graph[i][j] == 1 and graph[i + 1][j] == 1 and graph[i][j + 1] == 1 and graph[i + 1][j + 1] == 1:
            answer += 1

print(answer)       
