import math
import sys
input = sys.stdin.readline

n = str(input().rstrip())
cnt = 0
# 초기값, 처음인데 숫자 길이가 1인경우 대비
min_v = math.inf
max_v = 0

def command1(n):
    odd_n = 0
    for i in n:
        if int(i) % 2 == 1:
            odd_n +=1
    return odd_n

def solve(n, cnt):
    global max_v, min_v
    cnt += command1(n)

    if len(n) == 1:
        # 끝까지 가서 다 돌려본 것들 중 가장 많은 값
        min_v = min(min_v, cnt)
        max_v = max(max_v, cnt)
        return
    elif len(n) == 2:
        temp = str(int(n[0])+int(n[1]))
        solve(temp, cnt)
    else:
        # 구역을 나눈다 (8)(2)(019)//(8)(20)(19)//(8)(201)(9) ...계속
        # 82019는 3개의 구역 a,b,c로 나눈다.
        # a는 8부터0까지, b는 그보다 한 칸 뒤인 2부터 1까지, c는 한 칸 뒤인 0부터 끝까지 총 3개의 구역 지정
        for i in range(len(n)-2):
            for j in range(i+1,len(n)-1):
                a = n[:i+1]
                b = n[i+1:j+1]
                c = n[j+1:]
                # 재귀함수 계속 호출해서 모든 경우의 수에서 max와 min을 수정해준다.
                temp = str(int(a)+int(b)+int(c))
                solve(temp, cnt)

solve(n,0)
print(min_v, max_v)
