import sys
input = sys.stdin.readline

# 가로세로를 확인하는 함수, 대각선 확인하는 함수를 만든 후 인풋에 따라 기본 빙고판을 채운다.
# 사회자가 부르는 순서대로 하나씩 지워가면서 빙고인지 확인한다.

def check_line():
    bingo = 0
    for i in range(5):
        bool1 = True
        bool2 = True
        for j in range(5):
            # [j][i]는 세로 빙고를 세어준다. 하나라도 -1이 아니면 빙고 성립X
            if board[j][i] != -1:
                bool1 = False
            if board[i][j] != -1:
            # [i][j]는 가로 빙고를 세어준다. 하나라도 -1이 아니면 빙고 성립X 
                bool2 = False
        if bool1:
            bingo += 1
        if bool2:
            bingo += 1
    return bingo

def check_diagonal():
    bingo = 0
    bool1 = True
    bool2 = True
    for i in range(5):
        # 왼쪽 좌상단 대각선부터 시작
        if board[i][i] != -1:
            bool1 = False
        # 오른쪽 우상단 대각선부터 시작
        if board[i][4-i] != -1:
            bool2 = False
    if bool1:
        bingo += 1
    if bool2:
        bingo += 1
    return bingo

# 딕셔너리 이용
dic = dict()
board = []

# 빙고판 만들기
for i in range(5):
    li = list(map(int, input().split()))
    board.append(li)
    for j in range(5):
        dic[li[j]] = (i, j) #i행 j열에 값이 있음을 딕셔너리에 기록
        # ex) dic = {11 : (0,0) 12 : (0,1)...}
        # 딕셔너리는 key와 값 형태

# 사회자가 숫자를 부른다.
count = 0
flag = False
for _ in range(5):
    li = list(map(int, input().split()))
    for each in li:
        count+=1
        r, c = dic[each] #사회자가 부른 숫자를 key로 만들어서 dic에 전달, 그리고 key를 이용해 행,열을 알아냄
        board[r][c] = -1

        # 대각선 빙고와 가로세로 빙고 합이 3이상일 경우
        if(check_diagonal()+check_line()) >= 3:
            print(count)
            flag = True
            break
    if flag:
        break


