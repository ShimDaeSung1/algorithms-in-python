import sys
input = sys.stdin.readline

#에너지 드링크의 수
N = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
sum = 0

for i in range(0, N):
    if i == 0:
        sum += arr[0]
    else:
        sum += (arr[i]/2)
print(sum)
