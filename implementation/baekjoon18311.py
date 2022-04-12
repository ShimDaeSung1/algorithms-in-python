
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
li = list(map(int, input().split()))

for i in range(N):
    M -= li[i]
    if M < 0 :
        print(i+1)
        break
else:
    for i in range(N-1, -1, -1):
        M -= li[i]
        if M < 0:
            print(i+1)
            break
        
