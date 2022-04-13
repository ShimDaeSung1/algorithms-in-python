# import sys
# input = sys.stdin.readline

# N = int(input())
# find = int(input())
# board = [[0 for _ in range(N)]for _ in range(N)]

# # 우, 하, 좌, 상
# dr = [0, 1, 0, -1]
# dc = [1, 0, -1, 0]
# x = N//2 #시작X좌표
# y = N//2 #시작Y좌표

# num = 1 #해당 위치에 들어갈 숫자 1씩 증가 예정
# len  = 0 #특정 방향으로 이동할 길이 얼마나 더할지 for문으로 동일 작업 수행 가능

# board[x][y] = num #시작점을 1로 지정

# while True:
#     for i in range(4):
#         for _ in range(len): #특정 방향으로 한칸씩 이동하며 숫자 입력
#             x += dr[i]
#             y += dc[i]
#             num += 1
#             board[x][y] = num
#             if num == find :
#                 ans = [x+1, y+1]
#     if x==y==0:
#         break
#     x -= 1
#     y -= 1
#     len += 2

# for i in range(N):
#     # 리스트 앞에 *를 붙이면 언패킹
#     print(*board[i])
# print(*ans)


import sys
input = sys.stdin.readline

def draw():
    global n
    x = y = n//2
    # 첫 좌표 다음의 숫자
    len = num = 2
    # 이동, 우,하,좌,상으로 움직인다.
    d = [(0,1),(1,0),(0,-1),(-1,0)]
    # d를 사용할 때 쓸 인덱스
    t = 0 
    # 첫 좌표에 1을 찍는다.
    board[x][y] = 1
    # x와 y를 각각 1씩 낮춰 왼쪽 대각선 위로 이동한 후, 그 좌표부터
    #  우, 하, 좌, 상으로 똑같이 이동해주면 일정한 규칙대로 움직일 수 있다.
    x-=1
    y-=1

    while True:
        for _ in range(4):
            a, b = d[t]
            for _ in range(len):
                x += a
                y += b
                board[x][y] = num
                if num == m:
                    ans[0] = x+1
                    ans[1] = y+1
                # num이 최댓값(n^2)이 찍힐 경우
                if num == n**2:
                    return
                num += 1
            t = (t+1)%4
            len += 2
            x -= 1
            y -= 1

n = int(input())
m = int(input())
board = [[0 for _ in range(n)]for _ in range(n)]
ans = [n//2+1,n//2+1]
draw()
