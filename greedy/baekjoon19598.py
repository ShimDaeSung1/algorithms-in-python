import heapq
import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split()))for _ in range(N)]
arr.sort(key=lambda x : (x[0],x[1]))

room = []
heapq.heappush(room, arr[0][1])
for i in range(1, N):
    if room[0]<=arr[i][0]:
        heapq.heappop(room)
        heapq.heappush(room, arr[i][1])
    else:
        heapq.heappush(room, arr[i][1])

print(len(room))


