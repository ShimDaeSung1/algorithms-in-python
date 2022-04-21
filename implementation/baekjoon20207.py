import sys
input = sys.stdin.readline

calender = [0]*366

# 일정의 개수
N = int(input())
for _ in range(N):
    s, e = map(int, input().split())
    for i in range(s,e+1):
        calender[i] += 1

row = 0
col = 0
answer = 0
for i in range(len(calender)):
    if calender[i] != 0 :
        col = max(col, calender[i])
        row += 1
    else:
        answer += col*row
        row, col = 0, 0
answer += row*col
print(answer)
    



