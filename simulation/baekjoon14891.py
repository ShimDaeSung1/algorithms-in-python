from collections import deque
import sys
input = lambda:sys.stdin.readline().strip()

circle = [deque(map(int, input())) for _ in range(4)]
opers = deque(list(map(int, input().split())) for _ in range(int(input())))

while opers: #명령어가 남아있으면 반복문 실행
    num, direct = opers.popleft()
    num -= 1 #톱니바퀴는 1부터4, 실제 인덱스는 0부터 3이므로 -1
    tmp_2 = circle[num][2] # 비교 대상
    tmp_6 = circle[num][6] # 비교 대상
    circle[num].rotate(direct) # 시작 톱니부터 돌린다.
    tmp_direct = direct

    #시작 톱니 왼쪽
    direct = tmp_direct
    for i in range(num-1, -1, -1):
        if circle[i][2] != tmp_6:
            tmp_6 = circle[i][6]
            circle[i].rotate(direct*(-1))
            direct *= -1
        else:
            break
    #시작 톱니 오른쪽
    direct = tmp_direct
    for i in range(num+1, 4):
        if circle[i][6] != tmp_2:
            tmp_2 = circle[i][2]
            circle[i].rotate(direct*(-1))
            direct *= -1
        else:
            break
sum = 0
j = 1
for i in circle:
    if i[0] == 1:
        sum += (j*1)
    j*=2
print(sum)
    
