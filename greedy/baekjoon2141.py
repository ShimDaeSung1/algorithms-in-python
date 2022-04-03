import sys
input = sys.stdin.readline
from bisect import bisect_left

def cal_dist(position):
    dist = 0
    for town, population in arr:
        dist += abs(position-town)*population
    return dist

# 튜플은 리스트와 같지만 변경할 수 없다, 삭제도 불가능
N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]
left = -1000000000
right = 1000000000
answer = 0

# 이분탐색으로 무게중심을 찾고 그 좌우에 있는 마을만 거리비교해서 최솟값으로 가져간다.
# 둘의 거리가 같으면 왼쪽을 가져간다.
# 탐색할 범위가 남아있을동안 반복
while left <= right:
    mid = (left+right)//2
    if cal_dist(mid) < cal_dist(mid+1):
        right = mid - 1
        # 최솟값을 찾아야 하므로 작아질 때마다 값을 저장
        answer = mid
    else:
        left = mid + 1

arr.sort()
# bisect_left(a,x)는 정렬된 a에 x를 삽입할 위치를 리턴, x가 a에 이미 있으면 기존 항목의 앞(왼쪽)의 위치 반환
close_town_idx = bisect_left(arr,(answer,0))
if cal_dist(arr[close_town_idx-1][0]) == cal_dist(arr[close_town_idx][0]):
    answer = close_town_idx-1
else:
    answer = close_town_idx
print(arr[answer][0])


    
