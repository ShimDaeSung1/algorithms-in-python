import sys
input = sys.stdin.readline
import heapq

N = int(input())
heap = []

for _ in range(N):
    num_list = list(map(int, input().split()))
    if not heap: # heap에 아무것도 없을 때
        for num in num_list:
            heapq.heappush(heap, num) # 최소힙으로 채운다
    else:
        for num in num_list: # 힙에 값이 있다면 늘 힙의 길이를 n으로 유지한다.
            heapq.heappush(heap, num)
            heapq.heappop(heap)
print(heap)
