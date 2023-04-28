import sys
input = sys.stdin.readline
import heapq

#정점의 개수 v와 간선의 개수 e
v,e = map(int,input().split())
start = int(input())
distance = [float("inf")]*(v+1)
# 그래프들이 연결된 것
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    global distance
    distance[start] = 0
    # 거리가 가장 빠른 정점만 가져옴
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue

        for destination, time in graph[now]:
            cost = dist+time
            if cost < distance[destination]:
                distance[destination] = cost
                heapq.heappush(q, (cost, destination))   

dijkstra(start) 

for i in distance[1:]:
    if i == float("inf"):
        print("INF")
    else:
        print(i)
