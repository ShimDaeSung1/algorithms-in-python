import sys
input = sys.stdin.readline

N, M = map(int,input().split())

cakes = list(map(int,input().split()))
cakes.sort(key=lambda x : ((x%10),x))
count = 0

for cake in cakes :
    if M > 0 :
        if cake < 10 :
            continue
        elif cake == 10 :
            count+=1
            continue
        else: 
            if cake % 10 == 0  :
                cnt = (cake // 10)-1
                if cnt > M :
                    cnt = M
                    if cake == 20:
                        count += cnt+1
                    else:
                        count += cnt
                    M=0
                    continue
                else :
                    count += cnt+1
                    M -= cnt
                    continue
            else:
                cnt = cake // 10
                if cnt > M:
                    cnt = M
                    count += cnt
                    M -= cnt
                    continue
                else:
                    count += cnt
                    M -= cnt
                    continue
    else:
        break
print(count)


