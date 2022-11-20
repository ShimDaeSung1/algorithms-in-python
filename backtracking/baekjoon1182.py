import sys
input = sys.stdin.readline

n, s = map(int, input().split())
# 정수
cnt_list = list(map(int, input().split()))
cnt_list.sort()
answer_cnt = 0
ans = []
def backtracking(start):
    global answer_cnt
    if sum(ans) == s and len(ans) >0:
        answer_cnt+=1
    for i in range(start, n):
        ans.append(cnt_list[i])
        backtracking(i+1)
        ans.pop()

backtracking(0)
print(answer_cnt)
        

    


