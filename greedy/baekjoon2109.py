import heapq
import sys
input = sys.stdin.readline

N = int(input())
lecture = [list(map(int,input().split()))for _ in range(N)]
# 날짜 순서대로 오름차순 정렬
lecture.sort(key=lambda x : (x[1], x[0]))

queue = []

for pay, day in lecture:
    heapq.heappush(queue, pay)
    # 여태 진행한 날짜보다 기한이 낮으면 그 안에서 가장 낮은걸 빼준다.
    if day < len(queue):
        heapq.heappop(queue)
print(sum(queue))
        
        


