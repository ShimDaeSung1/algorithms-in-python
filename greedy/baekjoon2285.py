import sys
input = sys.stdin.readline
from bisect import bisect_left

def distance(x):
    distance = 0
    for i,j in arr:
        distance += abs(i-x)*j
    return distance

N = int(input())
arr = [tuple(map(int, input().split()))for _ in range(N)]

right = 1000000000
left = -1000000000
answer = 0
while left<=right:
    pivot = (right+left) // 2
    if distance(pivot)<distance(pivot+1):
        answer = pivot
        right = pivot-1
    else:
        answer = pivot
        left = pivot+1

arr.sort()

# bisect_left(a,x)는 정렬된 a에 x를 삽입할 위치를 리턴, x가 a에 이미 있으면 기존 항목의 앞(왼쪽)의 위치 반환
close_town_idx = bisect_left(arr,(answer,0))
if distance(arr[close_town_idx-1][0]) == distance(arr[close_town_idx][0]):
    answer = close_town_idx-1
else:
    answer = close_town_idx 

print(arr[answer][0])



