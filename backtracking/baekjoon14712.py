import sys

#행 개수, 열개수
n,m = map(int,sys.stdin.readline().split())

# 넴모가 올라갈 격자 판
graph = [[0 for _ in range(m)] for _ in range(n)]


#격자판 탐색 - node 는 넴모를 놓는 위치
def dfs(x,y:list)->int:
    #경우의 수 세기
    count = 0 
    #열이 격자판을 넘어가면 행을 하나 증가
    if y >= m:
        x = x+1
        y = 0
    #행을 증가했는데 격자판을 넘어가면 전부 탐색한 것임 - 탐색 끝
    if x >= n:
        return 0
    
    #넴모를 놓아도 터트릴수 없는 위치지면 놓고 다음 경우 탐색 - 3개중 한칸이라도 0이면 놓을수 있음
    if graph[x][y-1] ==0 or graph[x-1][y-1] == 0 or graph[x-1][y] == 0:
        #넴모를 놓음
        graph[x][y] = 1
        #네모를 놓은 상태에서 재귀를 이용해서 다음 경우 탐색하고, 그 결과에 현재 놓은 결과를 더해서 넣어줌
        count+=dfs(x,y+1)+ 1

        #다음 탐색을 위해서 놓았던 네모를 다시 빈칸으로 돌려놓음
        graph[x][y] = 0

    count += dfs(x,y+1)

    return count

print(dfs(0,0)+1)