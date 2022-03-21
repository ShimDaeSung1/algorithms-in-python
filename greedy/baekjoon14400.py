import sys
input = sys.stdin.readline

#주요 고객들의 수
N = int(input())

location = [list(map(int, input().split())) for _ in range(N)]

# x를 기준으로 정렬 후 중간값 정하기
middle_x = sorted(location, key = lambda x : x[0])[N//2][0]
middle_y = sorted(location, key = lambda x : x[1])[N//2][1]

res = 0

#중간값에서 각 주요 고객들의 위치 빼서 더하기
for i in location:
    res += (abs(middle_x-i[0]) + abs(middle_y-i[1]))

print(res)
