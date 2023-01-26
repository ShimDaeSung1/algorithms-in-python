import sys
input = sys.stdin.readline

k, n = map(int , input().split())
lansun = [int(input()) for _ in range(k)]

start = 0
end = max(lansun)

while start <= end:
    middle = (start+end)//2
    cnt = 0
    for i in lansun:
        cnt += i//middle
    
    if cnt >= n:
        start = middle+1
    elif cnt < n:
        end = middle-1

print(end)
        