import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    a,b = input().split()
    a = int(a,2)
    b = int(b,2)
    print(bin(a+b)[2:])
