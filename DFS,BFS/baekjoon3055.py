from collections import deque
from copy import deepcopy
import sys
input = sys.stdin.readline

dx = [0,0,1,-1]
dy = [1,-1,0,0]

R, C = map(int, input().split())

board = [list(input().strip()) for _ in range(R)]
visited = [[False]*C for _ in range(R)]
dic = dict()
flag = True
for i in range(R):
    for j in range(C):
        # 비버위치
        if board[i][j] == 'D' : 
            dic["D"] = [i,j]
            dic["D"].append(0)
        # 고슴도치 위치
        if board[i][j] == 'S' :
            dic['S'] = [i,j]
            dic['S'].append(0)
            visited[i][j] = True

queue = deque([])
queue.append(dic["S"])
answer = 9999
def bfs():
    global answer, board, visited
    while queue:
        # 지금 현재 queue에 들어있는 만큼만 for문 돌리고,
        # 다 돌리면 그 때 water 돌려야 정상적임,
        # 그 후 비버소굴에도 최솟값이 들어감
        for j in range(len(queue)):
            x,y,cur_cnt = queue.popleft()
            # print(x,y,cur_cnt)
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if 0<=nx<R and 0<=ny<C and visited[nx][ny] == False:
                    future = water()
                    if board[nx][ny] == '*' or future[nx][ny] == '*' or board[nx][ny] == 'X':
                        continue
                    if board[nx][ny] == '.' :
                        visited[nx][ny] = True
                        queue.append([nx,ny,cur_cnt+1])
                    if board[nx][ny] == 'D':
                        answer = min(answer, cur_cnt+1)
                        continue
        board = water()
        # for i in range(R):
        #     for j in range(C):
        #         print(board[i][j],end='')
        #     print()
    if answer == 9999:
        print("KAKTUS")
    else : 
        print(answer)
# 물 확장 시키기
def water():
    copy = deepcopy(board)
    visited2 = [[False]*C for _ in range(R)]
    q = deque([])
    for i in range(R):
        for j in range(C):
            if copy[i][j] == '*':
                q.append([i,j])
                visited2[i][j] = True
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<R and 0<=ny<C and visited2[nx][ny] == False and copy[nx][ny] == '.':
                copy[nx][ny] = '*'
                visited2[nx][ny] = True
    return copy
bfs()

