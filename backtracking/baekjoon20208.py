import sys
input = sys.stdin.readline

def backtracking(current, drink):
    global m,h,answer,start
    
    if abs(start[0]-current[0]) + abs(start[1]-current[1]) <= m:
        answer = max(answer, drink)
    
    for x,y in milk_list:
        #우유가 남아 있으면
        if graph[x][y] == 2:
            distance = abs(x-current[0]) + abs(y-current[1])
            #갈 수 있는 거리인지 확인
            if distance <= m:
                m = m - distance + h
                graph[x][y] = 0
                drink += 1
                backtracking([x,y], drink)
                m = m + distance - h
                graph[x][y] = 2
                drink -= 1
                
        

# 크기, 초기체력, 마실때마다 증가하는 체력
n,m,h = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
#집에서 다시 집으로 돌아올때까지 최대한 마실 수 있는 민트초코 개수
answer = 0
milk_list = []
start = [0,0]
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            start = [i,j]
        elif graph[i][j] == 2:
            milk_list.append([i,j])

backtracking(start, 0)
print(answer)




