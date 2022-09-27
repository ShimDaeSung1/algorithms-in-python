import sys
input =sys.stdin.readline

N = int(input())
cow = [list(map(int, input().split()))for _ in range(N)]
count = 0
cow_po = [-1]*11

for num, position in cow :
    if cow_po[num] == -1 :
        cow_po[num] = position
    else:
        if cow_po[num] != position:
            count+=1
            cow_po[num] = position
print(count)




