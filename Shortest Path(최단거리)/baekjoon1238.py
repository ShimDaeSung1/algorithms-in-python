import sys
input = sys.stdin.readline
import heapq

max_value = float("inf")

# n명의 학생이 X번 마을에 모인다. 마을 사이에는
# 총 m개의 단방향 도로들이 있다.
n,m,x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    start, end, t = map(int, input().split())
    graph[start].append((end, t))

def djikstra(start):
    q = []
    distance = [float("inf")]*(n+1)

    heapq.heappush(q,(0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        #기존에 구한 거리보다 새로 뽑은 거리가 크면
        if distance[now] < dist : 
            continue

        for definition, time in graph[now]:
            cost = dist + time
            # 새로 뽑은 거리가 더 작으면
            if distance[definition] > cost:
                distance[definition] = cost
                heapq.heappush(q, (distance[definition], definition))
    return distance

result = 0
for i in range(1, n+1):
    # i번 학생이 출발
    go = djikstra(i)
    back = djikstra(x) # 다시 돌아올땐 목표 마을에서부터
    result = max(result, go[x]+back[i])
print(result)

