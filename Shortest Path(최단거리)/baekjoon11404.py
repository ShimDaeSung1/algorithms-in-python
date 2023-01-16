import sys
input = sys.stdin.readline

#도시의 개수
n = int(input())
#버스의 개수
m = int(input())

#버스의 시작 도시, 도착 도시, 비용 c
buses = [list(map(int, input().split())) for _ in range(m)]

distance = [[float("inf") for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i==j:
            distance[i][j] = 0

for a,b,c in buses:
    a, b = a-1, b-1
    distance[a][b] = min(distance[a][b], c)

# 중간 노드
for j in range(n):
    for i in range(n):
        for k in range(n):
            dist = distance[i][j] + distance[j][k]
            if distance[i][k] > dist:
                distance[i][k] = dist

for i in range(n):
    for j in range(n):
        if distance[i][j] == float("inf") : 
            distance[i][j] = 0

for i in range(n):
    print(*distance[i])

