import heapq #힙을 사용한다. 파이썬에서 힙은 기본적으로 최소힙이다. 루트에 가장 낮은 값이 들어옴
import sys
input = sys.stdin.readline

# 최소힙은 root - left - right 순으로 삽입하고 자식과 부모를 비교하여 낮은 값이 위로 오도록 정렬한다
# 삭제는 가장 위(루트) 값부터 뽑는다. 그래서 최소값이 나온다
# heapq는 기본이 최소힙이기 때문에 오름차순으로 정렬된다.
# 시간 복잡도는 원소 삽입 : O(logN) / 삭제 : O(logN) 이다.

N = int(input())
C = [list(map(int,input().split()))for _ in range(N)]

C = sorted(C, key = lambda x : (x[0],x[1]))
# 빈 리스트를 생성한 후 heaqp 모듈의 함수 호출 시 리스트를 인자로 넘겨 최소 힙 자료구조로 동작하도록 한다.
room = []
heapq.heappush(room, C[0][1])

for i in range(1, N):
    if C[i][0] < room[0]: #현재 강의가 끝나는 시간보다 다음 강의 시작시간이 빠르면
        heapq.heappush(room, C[i][1]) # 새로운 강의실 개설
    if room[0] <= C[i][0] : #현재 강의실에 이어서 강의 가능
        heapq.heappop(room) #새로운 강의로 시간 변경을 위해 pop후 새 시간 push
        heapq.heappush(room, C[i][1])
print(len(room))






    
