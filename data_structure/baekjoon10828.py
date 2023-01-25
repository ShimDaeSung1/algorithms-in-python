import sys
input = sys.stdin.readline

stack = []

n = int(input())

answer = []
for _ in range(n):
    #명령
    go = input().split()

    if go[0] == "push":
        stack.append(int(go[1]))
    elif go[0] == "pop":
        if len(stack) == 0:
            answer.append(-1)
        else:
            answer.append(stack.pop())
    elif go[0] == "size":
        answer.append(len(stack))
    elif go[0] == "empty":
        if len(stack) == 0 :
            answer.append(1)
        else : 
            answer.append(0)
    elif go[0] == "top":
        if len(stack) >= 1:
            answer.append(stack[-1])
        else :
            answer.append(-1)
for i in answer:
    print(i)