import sys
input = lambda: sys.stdin.readline().strip()

# k년이 지난 후 살아남은 나무의 수 출력하기
n,m,k = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
# 양분 
eat = [[5]*n for _ in range(n)]

tree = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    # x,y,z 는 각각 행, 열, 나이
    x,y,z = map(int,input().split())
    tree[x-1][y-1].append(z)


#가을에 쓸 8방향
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

# K년 동안 4계절 진행
for i in range(k):
    # 봄 
    # 여름에 쓸 위치, 나이
    summer = []
    for x in range(len(tree)):
        for y in range(len(tree[x])):
            if len(tree[x][y]) > 0 :
                tree[x][y].sort()
                for o in range(len(tree[x][y])):
                    if eat[x][y] >= tree[x][y][o]:
                        eat[x][y] -= tree[x][y][o]
                        tree[x][y][o] += 1
                    else:
                        summer.append([x,y,tree[x][y][o]])
                        tree[x][y].pop(o)
    # 여름
    for x in summer:
        r, c, age_eat = x[0], x[1], x[2]
        eat[r][c] += age_eat//2
    
    # 가을
    for x in range(len(tree)):
        for y in range(len(tree[x])):
            if len(tree[x][y]) > 0 :
                # 번식
                for o in range(len(tree[x][y])):
                    if tree[x][y][o] % 5 == 0:
                        for z in range(8):
                            if 0<=x+dx[z]<n and 0<=y+dy[z]<n:
                                tree[x+dx[z]][y+dy[z]].append(1)
    #겨울 -> 양분 추가
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            eat[x][y] += arr[x][y]
answer = 0
for x in range(len(tree)):
    for y in range(len(tree[x])):
        answer += len(tree[x][y])          
print(answer)


    




#### 밑에는 풀이 다른사람꺼


from collections import deque
import sys
input = sys.stdin.readline
def spring():
    for i in range(n):
        for j in range(n):
            len_t = len(t[i][j])
            for k in range(len_t):
                if t[i][j][k] <= no[i][j]:
                    no[i][j] -= t[i][j][k]
                    t[i][j][k] += 1
                else:
                    # 어차피 정렬되어있으므로 양분보다 나이가 많은 나무가 나올 경우 
                    # 뒤 나무 수만큼 //2 해서 더해준다.
                    for _ in range(k, len_t):
                        no[i][j] += t[i][j].pop() // 2
                    break
def fall():
    for i in range(n):
        for j in range(n):
            for k in t[i][j]:
                if k % 5 == 0:
                    for l in range(8):
                        x = i + dx[l]
                        y = j + dy[l]
                        if 0 <= x < n and 0 <= y < n:
                            t[x][y].appendleft(1)
            no[i][j] += s[i][j]
dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, 1, -1, -1, 1]
n, m, k = map(int, input().split())
s = []
t = [[deque() for i in range(n)] for i in range(n)]
no = [[5] * n for i in range(n)]
for i in range(n):
    s.append(list(map(int, input().split())))
for i in range(m):
    x, y, z = map(int, input().split())
    t[x - 1][y - 1].append(z)
for i in range(k):
    spring()
    fall()
cnt = 0
for i in range(n):
    for j in range(n):
        cnt += len(t[i][j])
print(cnt)
