import heapq
import sys
input = sys.stdin.readline

# 강의의 개수 (<=100000)
N = int(input())
lecture = [list(map(int, input().split())) for _ in range(N)]
lecture.sort(key=lambda x : (x[1]))

room = []
heapq.heappush(room, lecture[0][2])

for i in range(1, N):
    if room[0]>lecture[i][1]:
        heapq.heappush(room, lecture[i][2])
        continue
    else:
        heapq.heappop(room)
        heapq.heappush(room, lecture[i][2])

print(len(room))





