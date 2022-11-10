from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

#치킨의 종류의 수는 최대 3가지 고를 수 있음
like = [list(map(int, input().split())) for _ in range(n)]
# like.sort(key = lambda x : -max(x))
arr = []
for i in range(m):
    arr.append(i)

chi = combinations(arr, 3)

max_value = 0
for a,b,c in chi:
    cnt = 0
    for i in range(len(like)):
        cnt += max(like[i][a], like[i][b], like[i][c])
    max_value = max(cnt, max_value)
print(max_value)
           


