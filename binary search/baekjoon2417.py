import sys
input = sys.stdin.readline

n = int(input())
start = 1
end = n

while start <= end :
    middle = (start+end)//2
    if middle**2 < n:
        start = middle+1
    elif middle**2 == n:
        print(middle)
        break
    else :
        end = middle-1

