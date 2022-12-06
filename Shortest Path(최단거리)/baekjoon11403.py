import sys
input = sys.stdin.readline
import heapq

N = int(input()) # 정점의 개수

graph = [list(map(int, input().split())) for _ in range(N)]
distance = [[float("inf") for _ in range(N+1)] for _ in range(N+1)]

def floyd_warshall():
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            distance[i+1][j+1] = graph[i][j]
    
    for k in range(1, N+1): #중간 노드(거치는 점)
        for i in range(1,N+1): #시작점
            for j in range(1,N+1): #끝나는점
                # if distance[i][j] > distance[i][k] + distance[k][j]:
                #     #중간을 거쳐가는 것이 더 빠를 경우
                #     distance[i][j] = distance[i][k]+distance[k][j]
                if distance[i][k] == 1 and distance[k][j]:
                    distance[i][j] = 1
floyd_warshall()
for i in range(1, N+1):
    for j in range(1, N+1):
        print(distance[i][j], end=" ")
    print()

        

    