from collections import deque
import sys
input = lambda: sys.stdin.readline().strip()

# N, K 길이N, 내구도 0인 칸의 개수 K
n, k = map(int,input().split())
# 내구도
belt = deque(map(int, input().split()))
robot = deque(0 for _ in range(n))

result = 0
while True:
    belt.rotate(1)
    robot.rotate(1)
    robot[-1] = 0
    for i in range(n-2, -1, -1):
        if robot[i] == 1:
            if robot[i+1] == 0 and belt[i+1]>= 1:
                robot[i] = 0
                if i+1 == n-1:
                    robot[i+1] = 0
                else:
                    robot[i+1] = 1
                belt[i+1] -= 1
    if belt[0] >= 1 and robot[0]==0:
        robot[0] = 1
        belt[0] -= 1
    result+=1
    if belt.count(0) >= k:
        break
print(result)










