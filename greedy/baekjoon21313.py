import sys
input = sys.stdin.readline

N = int(input())
num = 0
arr= []
if N % 2 == 0:
    for i in range(N//2):
        arr.append('1')
        arr.append('2')
    print(' '.join(arr))
else:
    for i in range(N//2+1):
        if i == N//2:
            arr.append('3')
            break
        else:
            arr.append('1')
            arr.append('2')
    print(' '.join(arr))
