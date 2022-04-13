import sys
input = sys.stdin.readline

N = int(input())
find = int(input())
board = [[0 for _ in range(N)]for _ in range(N)]

# 우, 하, 좌, 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
x = N//2 #시작X좌표
y = N//2 #시작Y좌표

num = 1 #해당 위치에 들어갈 숫자 1씩 증가 예정
len  = 0 #특정 방향으로 이동할 길이 얼마나 더할지 for문으로 동일 작업 수행 가능
# ans를 미리 N//2+1, N//2+1로 줘야한다. (꼭, 중요!)
ans = [N//2+1,N//2+1]
board[x][y] = num #시작점을 1로 지정
while True:
    for i in range(4):
        for _ in range(len): #특정 방향으로 한칸씩 이동하며 숫자 입력
            x += dr[i]
            y += dc[i]
            num += 1
            board[x][y] = num
            if num == find :
                ans[0] = x+1
                ans[1] = y+1
    if x==y==0:
        break
    x -= 1
    y -= 1
    len += 2

for i in range(N):
    # 리스트 앞에 *를 붙이면 언패킹
    print(*board[i])
print(*ans)
