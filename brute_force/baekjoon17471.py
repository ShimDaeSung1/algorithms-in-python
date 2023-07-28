import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations

def check(group):
    v = [False for _ in range(n+1)]
    queue = deque()
    queue.append(group[0])
    v[group[0]] = True
    while queue:
        q = queue.popleft()
        for i in range(1, n+1):
            #이어져있고 방문 가능시
            if graph[q][i] == 1 and v[i] == False and i in group:
                queue.append(i)
                v[i] = True
    
    for i in group:
        if v[i] == False:
            return False
    return True

def backtracking(group):
    global answer
    group_two = []
    group_two_sum = 0
    group_sum = 0
    for i in range(1, n+1):
        if i not in group:
            group_two.append(i)
            group_two_sum += population[i]
        else:
            group_sum += population[i]
    if check(group) == False or check(group_two) == False:
        return
    answer = min(answer, abs(group_sum - group_two_sum))

# 구역의 개수
n = int(input())

answer = float("inf")
population = list(map(int, input().split()))
population.insert(0,0)

graph = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    lst = list(map(int, input().split()))
    for j in range(1, len(lst)):
        graph[i][lst[j]] = 1
        graph[lst[j]][i] = 1

for i in range(1, n//2 + 1):
    comb = list(combinations(range(1, n+1), i))
    for com in comb:
        backtracking(com)

if answer == float("inf") : 
    print(-1)
    exit()
print(answer)


