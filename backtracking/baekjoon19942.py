import sys
input = sys.stdin.readline

MAX = float("inf")
answer = []
def check_min(lst):
    for i in range(4):
        if lst[i] < MIN[i]:
            return False
    return True

def backtracking(temp_answer, graph, visited, ans):
    global MAX, answer
    if check_min(temp_answer):
        if MAX > temp_answer[4]: 
            MAX = temp_answer[4]
            answer = ans
        elif MAX == temp_answer[4]:
            answer.append(ans)
        return
    for i in range(len(graph)):
        if visited[i] == False:
            for j in range(5):
                temp_answer[j] += graph[i][j]
            visited[i] = True
            ans.append(i+1)
            backtracking(temp_answer, graph, visited, ans)
            visited[i] = False
            ans.pop()
            for j in range(5):
                temp_answer[j] -= graph[i][j]

n = int(input())
mp, mf, ms, mv = map(int, input().split())
MIN = [mp,mf,ms,mv]
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [False for _ in range(len(graph))]
backtracking([0,0,0,0,0], graph, visited,[])

print(MAX)
print(answer)
