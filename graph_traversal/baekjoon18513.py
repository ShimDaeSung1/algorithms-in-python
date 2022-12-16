import sys
input = sys.stdin.readline
from collections import deque

# n개의 샘터, k개의 집 짓기
n, k = map(int, input().split())
water_location = list(map(int, input().split()))

visited = dict()

q = deque([])

for i in water_location:
    visited[i] = 1
    q.append([i,0])

answer = 0

def bfs():
    global q, k, answer

    while k>0 and q:
        now, dis = q.popleft()
        
        for i in [-1,1]:
            dn = now+i
            if dn not in visited and k>0: # 아무것도 없을 때
                visited[dn] = 1
                q.append([dn, dis+1])
                answer += dis+1
                k -= 1

bfs()
print(answer)


