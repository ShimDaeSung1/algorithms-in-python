import copy
import sys
input = lambda: sys.stdin.readline().strip()

# 50년 뒤 사라지는 섬이면 False, 살아있는 섬이면 True리턴
def survive_land(x, y, data_map):
    if data_map[x+1][y] + data_map[x-1][y] + data_map[x][y+1] + data_map[x][y-1] >= 3:
        return False
    else:
        return True

r,c = map(int, input().split())

# 바다 1
# 땅 0
# 지도와 지도 바깥부분도 바다로 감싸준다.
data_map = [[1]*(c+2) for i in range(r+2)]

# 땅의 위치 저장
land_loc = []

for i in range(r):
    data = input()

    for num, d in enumerate(data):
        # 땅이 들어오면 0으로 바꿈
        if d != ".":
            #바깥 부분을 추가해주었으므로 1씩 더해줌
            data_map[i+1][num+1] = 0
            land_loc.append([i+1, num+1])

# 얕은 복사를 하면 이전데이터를 변경하면 같이 변하므로 깊은 복사 진행
new_map = copy.deepcopy(data_map)
