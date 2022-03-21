import sys
input = sys.stdin.readline

#끝이 1이면 맨 끝의 1을 없애고, 아니면 2로 나눈다. 그러다가 
#어떤 방법을 써도 A보다 낮은 값이 되면, -1출력

A, B = map(int, input().split())
cnt=1
value = B

while value>A:
    if value % 10 == 1:
        value = value//10
        cnt+=1
        if(value<A):
            print('-1')
            break
    # 2로 나누어 떨어지지도 않고 끝이 1도 아니라면 -1출력
    elif value % 2 == 1 and value % 10 != 1:
        print('-1')
        break
    else : 
        value = value//2
        cnt+=1
        if(value<A):
            print('-1')
            break
    if value == A :
        print(cnt)
        break 





