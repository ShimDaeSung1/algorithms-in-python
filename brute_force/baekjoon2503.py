from itertools import combinations
import sys
input = sys.stdin.readline
from itertools import permutations

# 질문의 수
n = int(input())

arr = []
for _ in range(n):
    #민혁이가 물어본 숫자, 스트라이크, 볼
    a,b,c = map(int, input().split())
    arr.append([a,b,c])

ar = [i for i in range(1,10)]
com = permutations(ar, 3)

answer = 0
for i in com:
    cnt = 0
    for j in range(len(arr)):
        number, strike, ball = str(arr[j][0]), arr[j][1], arr[j][2]
        str_cnt = 0
        bal_cnt = 0
        for k in range(len(number)):
            #스트라이크 개수 세기
            if str(i[k]) == number[k] :
                str_cnt += 1
            else :
                if k == 0 :
                    if str(i[k]) == number[k+1] or str(i[k]) == number[k+2]:
                        bal_cnt += 1
                if k == 1:
                    if str(i[k]) == number[k-1] or str(i[k]) == number[k+1]:
                        bal_cnt +=1
                if k == 2:
                    if str(i[k]) == number[k-1] or str(i[k]) == number[k-2]:
                        bal_cnt +=1
        if str_cnt == strike and bal_cnt == ball:
            cnt +=1
    if cnt == len(arr):
        answer += 1
print(answer)




    
