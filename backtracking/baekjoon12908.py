import sys
input = sys.stdin.readline

def backtracking(xs, ys, xe, ye, teleport, visited, count):
    global answer
    # 텔레포트된 곳에서 목적지까지 거리 계산 
    answer = min(answer, count + (abs(xs-xe)+abs(ys-ye)))
    
    #텔레포트 돌기
    for i in range(6):
        # 쓴 텔레포트가 아님과 동시에 직전 위치랑 다를 경우에 가능
        if visited[i] == False :
            start_x, start_y, end_x, end_y = teleport[i]
            # 텔레포트 했으므로 10초 증가, 해당 위치까지 가서 텔레포트
            count += (10 + (abs(xs-start_x)+abs(ys-start_y)))
            visited[i] = True
            backtracking(end_x, end_y, xe, ye, teleport, visited, count)
            visited[i] = False
            count -= (10 + (abs(xs-start_x)+abs(ys-start_y)))
    
xs, ys = map(int, input().split())
xe, ye = map(int, input().split())
visited = [False]*6

teleport = []

for i in range(3):
    a, b, c, d = map(int, input().split())
    teleport.append([a,b,c,d])
    teleport.append([c,d,a,b])

answer = float("inf")
backtracking(xs, ys, xe, ye, teleport, visited, 0)
# 텔레포트 3개 갖고 백트래킹, 각 텔레포트를 쓴 후, 다시 제자리로 돌아가는 경우는 없어야함. 
# 그리고 쓸 때마다 텔레포트를 더 쓸 때와 안 쓰고 갈 때의 거리 계산을 해줄 것.

print(answer)
