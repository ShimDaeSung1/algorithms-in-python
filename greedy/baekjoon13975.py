import heapq
import sys
input = sys.stdin.readline

T = int(input())


for _ in range(T):
    n = int(input())
    pages = list(map(int, input().split()))
    min_heap = []
    ans = 0

    for i in pages:
        heapq.heappush(min_heap, i)
    while len(min_heap)>1:
       a = heapq.heappop(min_heap)
       b = heapq.heappop(min_heap)
       ans += a+b
       heapq.heappush(min_heap, a+b)
    print(ans)
       


    
    





