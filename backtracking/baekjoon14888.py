import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 수의 개수
n = int(input())

# 수열
numbers = list(map(int, input().split()))

# 덧셈, 뺄셈, 곱셈, 나눗셈
S = list(map(int, input().split()))

def plus(a,b):
    return a+b

def minus(a,b):
    return a-b

def X(a,b):
    return a*b

def Y(a,b):
    if (a<0 and b>0) or (a>0 and b<0):
        return -(abs(a)//b)
    else:
        return a//b
answer = []
def backtracking(now_value, index):
    global numbers, answer
    
    if index == n-1:
        answer.append(now_value)
        return

    for j in range(len(S)):
        if S[j]>0:
            temp = now_value
            if j == 0: # 덧셈
                now_value = plus(now_value, numbers[index+1])
                S[j] -= 1
            if j == 1: # 뺄셈
                now_value = minus(now_value, numbers[index+1])
                S[j] -= 1
            if j == 2: # 곱셈
                now_value = X(now_value, numbers[index+1])
                S[j] -= 1
            if j == 3: # 나눗셈
                now_value = Y(now_value, numbers[index+1])
                S[j] -= 1
            backtracking(now_value, index+1)
            now_value = temp
            S[j] += 1
backtracking(numbers[0],0)
print(max(answer))
print(min(answer))


