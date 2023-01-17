import sys
input = sys.stdin.readline
from copy import deepcopy
from itertools import permutations, combinations
char = str(input().strip())

# 전공책 개수
n = int(input().strip())
arr = []
for _ in range(n):
    cost, str = input().split()
    arr.append([cost,str])

answer = float("inf")

def check(cnt):
    #경우의 수
    comb = [i for i in range(len(arr))]
    gg = combinations(comb, cnt)
    visited = [False]*len(char)

    for i in gg:
        cost = 0
        str = ""
        for j in i:
            str += arr[j][1]
            cost += int(arr[j][0])
        array = permutations(list(str), len(char))
        flag = True
        for c in char:
            if c not in array:
                flag = False
        if flag == True:
            answer = min(answer, cost)
for i in range(1, len(char)+1):
    check(i)
print(answer)

    

                


        



