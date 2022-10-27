import sys
input = sys.stdin.readline

S = int(input())
n = 1
# 1+2+3+...+n = n(n+1)/2
while n*(n+1)/2 <= S:
    n += 1
print(n-1)