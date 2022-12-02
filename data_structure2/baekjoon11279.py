import sys
input = sys.stdin.readline
import heapq

#힙을 tuple로 구성할 경우 맨 앞 숫자만 가지고 정렬한다.
#절댓값 정렬시에 앞은 절댓값, 뒤는 원래값으로 한다 

N = int(input())
lst = []
heap = []
for i in range(N):
    cnt = int(input())

    if cnt == 0:
        try :
            print(-1*heapq.heappop(heap))
        except:
            print(0)

    else:
        heapq.heappush(heap, -cnt)