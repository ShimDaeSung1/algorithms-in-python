import sys
input = sys.stdin.readline

N = int(input())
card = list(map(int, input().split()))
card.sort()

M = int(input())
check = list(map(int, input().split()))

for i in check:
    start = 0
    end = len(card)-1
    flag = False
    while start <= end:
        center = (start+end)//2
        if card[center] == i :
            flag = True
            break
        else:
            if i > card[center]:
                start = center+1
            elif i < card[center]:
                end = center-1
    if flag : print(1, end=" ")
    else : print(0, end=" ")

