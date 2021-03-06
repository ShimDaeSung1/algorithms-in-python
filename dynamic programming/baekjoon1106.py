import sys

input = sys.stdin.readline
INF = 1e9

c, n = map(int, input().split())
data = []

min_cost = [INF]*(c+100)
min_cost[0] = 0

for _ in range(n):
    #cost, cus
    data.append(list(map(int, input().split())))

#cost 작은순 정리
data.sort(key=lambda x : x[1])
for cost, cus in data :
    for i in range(cus, c+100):
        min_cost[i] = min(min_cost[i-cus]+cost, min_cost[i])
print(min(min_cost[c:]))
