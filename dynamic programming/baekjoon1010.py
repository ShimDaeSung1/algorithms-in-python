def factorial(n):
    num = 1
    for i in range(1,n+1):
        num *= i
    return num


t = int(input())

# mCn : m개 지역에 n개의 다리를 놓을 수 있는 경우의 수
for _ in range(t):
    n, m  = map(int, input().split())
    bridge = factorial(m)//(factorial(m-n)*factorial(n))
    print(bridge)
