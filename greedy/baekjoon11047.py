import sys
input = sys.stdin.readline

N, sum = map(int,input().split())
coin = []
for i in range(N):
    coin.append(int(input()))

coin.sort(reverse=True)

count=0
for i in range(N):
    if coin[i]<sum:
        count += sum//coin[i]
        sum %= coin[i]
    elif coin[i]==sum:
        count+=1
        break

print(count)
