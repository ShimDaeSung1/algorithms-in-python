import sys
input = sys.stdin.readline

# 2차원 세계의 세로 길이 H와 가로 길이 W
Height, Width = map(int, input().split())
block = list(map(int, input().split()))
ans = 0

#첫번째와 마지막은 물이 찰 수 없으므로 범위는 1~width-1
for i in range(1, Width-1):
    left_max = max(block[:i])
    right_max = max(block[i+1:])

    # 자신을 기준으로 왼쪽 중 가장 큰 기둥과 오른쪽 중 가장 큰 기둥 중에
    # 더 낮은 기둥만큼 물을 채워줘야한다.
    water = min(left_max, right_max)
    if block[i] < water:
        ans += water-block[i]
print(ans)



