# pypy3
import sys
input = sys.stdin.readline

# 크레인의 수
crain_N = int(input())
# 크레인의 무게제한
crain_h = list(map(int, input().split()))

# 박스의 수
box_N = int(input())
# 박스의 무게
box_h = list(map(int, input().split()))

crain_h.sort(reverse=True)
box_h.sort(reverse=True)

if crain_h[0] < box_h[0]:
    print(-1)
    sys.exit()

minute = 0

# 더이상 옮겨질 물건이 없을 때 까지
while len(box_h)>0:
    for i in crain_h:
        for j in range(len(box_h)):
            if i >= box_h[j]:
                box_h.pop(j)
                break
    minute+=1
print(minute)



