import sys
input = sys.stdin.readline
from collections import deque

def dfs(current, dice_cnt):
    global answer
    q = deque([])
    q.append([current, dice_cnt])
    while q:
        x, cnt = q.popleft()
        if x == 100:
            answer = cnt
            break
        for i in range(1,7):
            destination = x+i
            # 너비우선 탐색이므로, 이미 간 곳이라면 나보다 더 짧은 카운트로 갔던 곳. 다시 탐색 필요 X
            if destination > 100 or visited[destination] == True: continue
            visited[destination] = True
            q.append([graph[destination], cnt+1])

# 사다리, 뱀 수(사다리는 위, 뱀은 아래)
n,m = map(int, input().split())

graph = [i for i in range(101)] # 0부터 100까지 있음
visited = [False for _ in range(101)]
for _ in range(n):
    # 사다리
    x,y = map(int, input().split())
    graph[x] = y

for _ in range(m):
    # 뱀
    x,y = map(int, input().split())
    graph[x] = y

# 1번칸에서 시작, 100번 칸에 도착할때까지 최소한의 주사위 수
dice = [1,2,3,4,5,6]
answer = float("inf")
dfs(1,0)
print(answer)
