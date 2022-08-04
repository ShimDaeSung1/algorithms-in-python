from collections import deque
import statistics


#인접한 방향 동서남북, 그리고 범위 벗어날 시 첫번째-마지막 이어줌.
dx = [-1,0,1,0]
dy = [0,1,0,-1]

n,m,t = map(int, input().split())
board = [[]]
deque(board)

for _ in range(n):
    lst = list(map(int, input().split()))
    board.append(deque(lst))
# 명령
command = []
for _ in range(t):
    command.append(list(map(int, input().split())))
# 원판 회전
for i in command:
    x, d, k = i
    counting = 0
    for j in range(1, n+1):
        if j % x == 0:
            if d == 0 :
                board[j].rotate(k)
            else : 
                board[j].rotate(-k)

     # 원판에 수가 있을 경우
    temp_num = 0
    for num in board:
        temp_num += sum(num)      
    if temp_num == 0:
        break
    visited = [[0] * (m) for _ in range(n+1)]
    for r in range(1, n+1):
        for c in range(m):
            if board[r][c] == 0 or visited[r][c] == 1:
                continue
            queue = [(r,c)]
            while queue:
                kr, kc = queue.pop()
                for k in range(4):
                    current_r = kr + dx[k]
                    current_c = kc + dy[k]
                    # 열끼리 연산
                    if current_c < 0:
                        current_c = m - 1
                    elif current_c > m - 1:
                        current_c = 0
                    if 1 <= current_r and current_r < n+1 and visited[current_r][current_c] == 0:
                        # 인접한 것끼리 숫자가 같을 경우
                        if board[kr][kc] == board[current_r][current_c]:
                            # 방문 처리
                            visited[kr][kc] = 1
                            visited[current_r][current_c] = 1
                            queue.append((current_r, current_c))
    # visited한 것이 있으면 == 인접한 것이 있으면 0으로 만듦.
    check = 0
    for rr in range(1, n+1):
        for cc in range(m):
            if visited[rr][cc] == 1:
                board[rr][cc] = 0
                check = 1
    if check == 0 :
        avg = 0
        cnt = 0
        # 평균 계산
        for rr in range(1, n+1):
            for cc in range(m):
                if board[rr][cc] != 0:
                    avg += board[rr][cc]
                    cnt += 1
        avg /= cnt
        for rr in range(1,n+1):
            for cc in range(m):
                if board[rr][cc] != 0:
                    # 평균보다 크면 1 빼줌
                    if board[rr][cc] > avg:
                        board[rr][cc] -= 1
                    # 평균보다 작으면 1 더해줌
                    elif board[rr][cc] < avg:
                        board[rr][cc] += 1
answer = 0

for i in board:
    answer += sum(i)
print(answer)
                



    
