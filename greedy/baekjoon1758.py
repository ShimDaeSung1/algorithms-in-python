import sys
input = sys.stdin.readline

#스타벅스 앞에 서 있는 사람의 수
N = int(input())

tip = 0
arr = []

for i in range(N):
    a = int(input())
    arr.append(a)
arr.sort(reverse=True)

for i in range(N):
    if arr[i]-(i)>=0:
        tip += (arr[i]-i)
    else: 
        continue

print(tip)    