n, m = map(int, input().split())

def factorial(num):
    if num <= 1:
        return 1
    return factorial(num-1)*num

print(factorial(n)//(factorial(n-m)*factorial(m)))

# import sys
# fac = [1, 1, 2]
# n, m = map(int, sys.stdin.readline().rsplit())

# for i in range(3, n + 1):
# 	fac.append(fac[i - 1] * i)

# print(fac[n] // (fac[m] * fac[n - m]))
