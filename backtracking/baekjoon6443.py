import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
# 개수
n = int(input())
answers = set()

def backtracking(stack, lst, visited):
    global answers
    if len(stack) == len(lst):
        answers.add(''.join(map(str, stack)))
        return
    
    for i in range(len(lst)):
        if visited[i] == False:
            stack.append(lst[i])
            visited[i] = True
            backtracking(stack, lst, visited)
            stack.pop()
            visited[i] = False

for _ in range(n):
    lst = list(input().strip())
    stack = []
    visited = [False]*len(lst)
    backtracking(stack, lst, visited)

answer = list(answers)
# for i in answers:
#     answer.append(i)
answer.sort(key = lambda x : (len(x), x))

for i in answer:
    print(i)


