import sys
input = sys.stdin.readline

for i in range(int(input())):
    p = int(input())
    a = str(input())
    b = str(input())
    W, B= 0,0
    for j in range(p):
         if a[j]!=b[j]:
            if b[j] == 'W':
                 W+=1
            else:
                 B+=1
    print(max(W,B))


