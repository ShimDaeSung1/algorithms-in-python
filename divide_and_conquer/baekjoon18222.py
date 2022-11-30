import sys, math
input = sys.stdin.readline

k = int(input())
def divide_and_conquer(n,k):

    num = math.log(k,2)
    # 2의 제곱으로 나누어 떨어질경우
    if num == int(num):
        if n == 0:
            print(int(num%2))
            exit()
        if n == 1:
            print(int(num%2)+1)
            exit()
    
    # 떨어지지 않으면 
    a = k-(2**int(num))
    b = 0
    #시작하는 숫자를 n으로 주기
    if int(num) % 2 == 0:
        b = 0
    else : 
        b = 1

    divide_and_conquer(b, a)

divide_and_conquer(0,k)

    



    


        