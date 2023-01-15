import sys, math
input = sys.stdin.readline

n = int(input())

def divide_and_conquer(n,k):

    if n == 1:
        print(k)
        exit()
    
    num = math.log(n,2)

    if num == int(num):
        if num % 2 == 0:
            print(k)
            exit()
        else:
            print(1-k)
            exit()

    else:
        num = int(num)
    divide_and_conquer(n-2**num, 1-k)

divide_and_conquer(n,0)