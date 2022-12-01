import sys
input = sys.stdin.readline
from copy import deepcopy
from itertools import combinations

# 모눈종이 크기
h, w = map(int, input().split())
n = int(input())

sticker = [list(map(int, input().split())) for _ in range(n)]
stc = [i for i in range(len(sticker))]
arr = list(combinations(stc, 2))

result = 0

for i in arr:
    a, b = i
    r1, c1 = sticker[a]
    r2, c2 = sticker[b]
    if (r1 + r2 <= h and max(c1, c2) <= w) or (max(r1, r2) <= h and c1 + c2 <= w):
            result = max(result, r1*c1 + r2*c2)
    if (c1 + r2 <= h and max(r1, c2) <= w) or (max(c1, r2) <= h and r1 + c2 <= w):
        result = max(result, r1*c1 + r2*c2)
    if (c1 + c2 <= h and max(r1, r2) <= w) or (max(c1, c2) <= h and r1 + r2 <= w):
        result = max(result, r1*c1 + r2*c2)
    if (r1 + c2 <= h and max(c1, r2) <= w) or (max(r1, c2) <= h and c1 + r2 <= w):
        result = max(result, r1*c1 + r2*c2)
print(result)