import sys
input = sys.stdin.readline

# 문제의 수
N = int(input())
color = str(input())


B = color.count('B')
R = color.count('R')

#B,R
count = [0,0]

if color[0] == 'B':
    count[0]+=1
else : 
    count[1]+=1

for i in range(1, N):
    if color[i] != color[i-1]:
        if color[i] == 'B':
            count[0] += 1
        else :
            count[1] += 1

print(count)