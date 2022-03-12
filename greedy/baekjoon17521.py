import sys
input = sys.stdin.readline

#n은 요일 수, w는 초기현금
n, w = map(int, input().split())

money = w
coin = 0
arr = []
for i in range(n):
    data = int(input())
    arr.append(data)

for i in range(1, n):
    if coin == 0 :
        if arr[i]>arr[i-1]:
            coin += (money//arr[i-1])
            money -= coin*arr[i-1]
    else :
        if arr[i-1]>arr[i]:
            money += coin*arr[i-1]
            coin = 0
if coin:
    money += coin*arr[n-1]
print(money)       